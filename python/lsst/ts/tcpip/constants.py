# This file is part of ts_tcpip.
#
# Developed for the Rubin Observatory Telescope and Site System.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__all__ = [
    "DEFAULT_MONITOR_CONNECTION_INTERVAL",
    "LOCALHOST_IPV4",
    "LOCALHOST_IPV6",
    "LOCALHOST",
    "LOCAL_HOST",
    "TERMINATOR",
]

# Default interval between checks if the connection is alive (seconds)
DEFAULT_MONITOR_CONNECTION_INTERVAL = 0.1

# localhost constants for IPV4 and IPV6
LOCALHOST_IPV4 = "127.0.0.1"
LOCALHOST_IPV6 = "::1"
# The default localhost
LOCALHOST = LOCALHOST_IPV4
# Deprecated alias to LOCALHOST
LOCAL_HOST = LOCALHOST

# The standard TCP/IP line terminator (bytes)
TERMINATOR = b"\r\n"
