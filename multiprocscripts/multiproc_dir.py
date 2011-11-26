"""
:mod:`multiproc_dir` -- Allows to start a script on multiple files
==================================================================

.. moduleauthor:: Raphael Vinot
"""

import subprocess
import os
import glob
import time

__license__ = """
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2011 Raphael Vinot

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
"""


class MultiprocDir(object):
    """
    Allows to start a script on multiple files

    :type max_spawn: int >= 1

    :param max_spawn: Max amount of processes to run at the same time. \
    This should be something like between Number of CPU and Number of CPU * 2

    :type launcher: String

    :param launcher: Path to the the program used to launch you script.

    :type sleep_time: int >= 1

    :param sleep_time: Interval to verify that the max amount of processes are \
    running.
    """

    def __init__(self, max_spawn = 1, launcher="/usr/bin/python", sleep_time = 10):
        self.launcher = launcher
        self.max_spawn = max_spawn
        self.sleep_time = sleep_time

    def spawn_scripts(self, script, path, files_pattern="*"):
        """Spawn the scripts and ensure the max amount of processes is running.

        :param script: Filename of the script to run.
        :param path: Path to the directory with the files to parse.
        : param files_pattern: Pattern to match the correct files.
        """
        processes = []
        print os.path.join(path, files_pattern)
        for infile in glob.glob( os.path.join(path, files_pattern) ):
            print self.launcher + " "  + script + " " + infile
            processes.append(subprocess.Popen([self.launcher, script, infile]))
            processes = self.check_processes(processes)
        self.check_processes(processes, True)
        print "Finished."

    def check_processes(self, processes, everything_started = False):
        """Check the list of running processes.

        :param processes: the list of running processes (pids)
        :return: The new process list, without the finished one.
        """
        while len(processes) >= self.max_spawn or everything_started:
            for p in processes:
                if p.poll() is not None:
                    processes.remove(p)
            time.sleep(self.sleep_time)
            if len(processes) == 0:
                break
        return processes

