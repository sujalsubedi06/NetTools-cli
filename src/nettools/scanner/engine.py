"""
TCP connect scanner engine.
"""

from __future__ import annotations

import socket
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

from nettools.core.constants import DEFAULT_TIMEOUT, DEFAULT_WORKERS
from nettools.scanner.models import PortResult
from nettools.scanner.services import get_service_name


class TCPScanner:
    """
    TCP Connect scanner.

    Performs authorized TCP port checks against a target host.
    """

    def __init__(
        self,
        timeout: float = DEFAULT_TIMEOUT,
        workers: int = DEFAULT_WORKERS,
    ) -> None:
        """
        Initialize scanner.

        Args:
            timeout: Connection timeout in seconds.
            workers: Maximum concurrent workers.
        """

        self.timeout = timeout
        self.workers = workers

    def scan_port(
        self,
        host: str,
        port: int,
    ) -> PortResult:
        """
        Scan a single TCP port.

        Args:
            host: Target hostname or IP.
            port: TCP port number.

        Returns:
            PortResult object.
        """

        start_time = time.perf_counter()

        is_open = False

        try:
            with socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM,
            ) as sock:
                sock.settimeout(self.timeout)

                result = sock.connect_ex((host, port))

                is_open = result == 0

        except socket.error:
            is_open = False

        elapsed = time.perf_counter() - start_time

        return PortResult(
            host=host,
            port=port,
            is_open=is_open,
            service=get_service_name(port),
            response_time=elapsed,
            scanned_at=datetime.now(),
        )

    def scan(
        self,
        host: str,
        ports: list[int],
    ) -> list[PortResult]:
        """
        Scan multiple ports.

        Args:
            host: Target hostname or IP.
            ports: Ports to scan.

        Returns:
            List of port results.
        """

        results: list[PortResult] = []

        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            futures = [
                executor.submit(
                    self.scan_port,
                    host,
                    port,
                )
                for port in ports
            ]

            for future in as_completed(futures):
                results.append(future.result())

        return sorted(
            results,
            key=lambda result: result.port,
        )


__all__ = [
    "TCPScanner",
]
