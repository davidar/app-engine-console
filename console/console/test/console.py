#!/usr/bin/env python
#
# console.py - Unit tests for the console module
#
# Copyright 2008-2009 Proven Corporation Co., Ltd., Thailand
#
# This file is part of App Engine Console.
#
# App Engine Console is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# App Engine Console is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with App Engine Console; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import sys
import unittest
import test_environment

from appengine_test import AppEngineTest
from console.app import model

class AppEngineConsoleTestCase(AppEngineTest):
    def setUp(self):
        AppEngineTest.setUp(self)
        self.engine = model.AppEngineConsole()

    def assertOutput(self, str, msg=''):
        self.assertEqual(self.engine.out.strip(), str, msg)

    def testTest(self):
        self.assert_(True)

    def testSimplestStatementThrowsNoExceptions(self):
        self.engine.runsource('')

    def testBasicStatements(self):
        self.engine.runsource('')
        self.assertOutput('')

        self.engine.runsource('5')
        self.assertOutput('5')

        self.engine.runsource('8 * 3')
        self.assertOutput('24')

    def testAssignmentStatements(self):
        self.engine.runsource('foo = 23')
        self.assertOutput('')

        self.engine.runsource('print foo')
        self.assertOutput('23')

        self.engine.runsource('foo')
        self.assertOutput('23')

def suite():
    s = unittest.TestSuite()
    s.addTest( unittest.makeSuite(AppEngineConsoleTestCase, 'test') )
    return s

if __name__ == "__main__":
    unittest.main()
