# Purpose: Unit tests for Calculate class to calculate RPM and MPH values
#
# Author:      Arno E Jones
#
# Created:     12/07/2018, 2019
# Copyright:   (c) jonesar 2018, 2019
# Licence:     This code can be freely shared and modified as long as the author is credited with the original (this) version.
# -------------------------------------------------------------------------------

import unittest
import Calculate

class TestGearSplitter(unittest.TestCase):
    ##################### Calculate for RPM #########################
    def test_5thGear_noTransferCase_For_Rpm(self):
        expected = [[0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500],
                    [0.0, 13.1, 26.3, 39.4, 52.5, 65.6, 78.8, 91.9, 105.0, 118.1, 131.3, 144.4, 157.5, 170.6]]
        result = Calculate.JeepGearSplitter.calculateSpeedFromRpm(jeep_model='jk',
                                                                  differentialGearRatio=4.56,
                                                                  tireDiameter=33.4,
                                                                  gearSelected=5,
                                                                  transmissionType='automatic',
                                                                  rubicon=True,
                                                                  fourLowEngaged=False)
        self.assertEqual(result, expected)

    def test_5thGear_transferCaseEngaged_nonRubicon(self):
        expected = [[0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500],
                    [0.0, 4.8, 9.7, 14.5, 19.3, 24.1, 29.0, 33.8, 38.6, 43.4, 48.3, 53.1, 57.9, 62.7]]
        result = Calculate.JeepGearSplitter.calculateSpeedFromRpm(jeep_model='jk',
                                                                  differentialGearRatio=4.56,
                                                                  tireDiameter=33.4,
                                                                  gearSelected=5,
                                                                  transmissionType='automatic',
                                                                  rubicon=False,
                                                                  fourLowEngaged=True)

        self.assertEqual(result, expected)

    def test_5thGear_transferCaseEngaged_Rubicon(self):
        expected = [[0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500],
                    [0.0, 3.3, 6.6, 9.8, 13.1, 16.4, 19.7, 23.0, 26.3, 29.5, 32.8, 36.1, 39.4, 42.7]]
        result = Calculate.JeepGearSplitter.calculateSpeedFromRpm(jeep_model='jk',
                                                                  differentialGearRatio=4.56,
                                                                  tireDiameter=33.4,
                                                                  gearSelected=5,
                                                                  transmissionType='automatic',
                                                                  rubicon=True,
                                                                  fourLowEngaged=True)

        self.assertEqual(result, expected)

    def test_1stGear_transferCaseEngaged_Rubicon(self):
        expected = [[0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500],
                    [0.0, 3.3, 6.6, 9.8, 13.1, 16.4, 19.7, 23.0, 26.3, 29.5, 32.8, 36.1, 39.4, 42.7]]
        result = Calculate.JeepGearSplitter.calculateSpeedFromRpm(jeep_model='jk',
                                                                  differentialGearRatio=4.56,
                                                                  tireDiameter=33.4,
                                                                  gearSelected=5,
                                                                  transmissionType='automatic',
                                                                  rubicon=True,
                                                                  fourLowEngaged=True)

        self.assertEqual(result, expected)

    def test_1stGear_transferCaseEngaged_nonRubicon(self):
        expected = [[0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500],
                    [0.0, 3.3, 6.6, 9.8, 13.1, 16.4, 19.7, 23.0, 26.3, 29.5, 32.8, 36.1, 39.4, 42.7]]
        result = Calculate.JeepGearSplitter.calculateSpeedFromRpm(jeep_model='jk',
                                                                  differentialGearRatio=4.56,
                                                                  tireDiameter=33.4,
                                                                  gearSelected=5,
                                                                  transmissionType='automatic',
                                                                  rubicon=True,
                                                                  fourLowEngaged=True)

        self.assertEqual(result, expected)

    def test_reverseGear_transferCaseEngaged_Rubicon_automatic(self):
        expected = [[0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500],
                    [0.0, 4.8, 9.7, 14.5, 19.3, 24.1, 29.0, 33.8, 38.6, 43.4, 48.3, 53.1, 57.9, 62.7]]
        result = Calculate.JeepGearSplitter.calculateSpeedFromRpm(jeep_model='jk',
                                                                  differentialGearRatio=4.56,
                                                                  tireDiameter=33.4,
                                                                  gearSelected=5,
                                                                  transmissionType='automatic',
                                                                  rubicon=False, fourLowEngaged=True)

        self.assertEqual(result, expected)

    def test_reverseGear_transferCaseEngaged_Rubicon_manual(self):
        expected = [[0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500],
                    [0.0, 4.8, 9.7, 14.5, 19.3, 24.1, 29.0, 33.8, 38.6, 43.4, 48.3, 53.1, 57.9, 62.7]]
        result = Calculate.JeepGearSplitter.calculateSpeedFromRpm(jeep_model='jk',
                                                                  differentialGearRatio=4.56,
                                                                  tireDiameter=33.4,
                                                                  gearSelected=5,
                                                                  transmissionType='automatic',
                                                                  rubicon=False,
                                                                  fourLowEngaged=True)

        self.assertEqual(result, expected)

    def test_4thGear_transferCaseNotEngaged_nonRubicon(self):
        expected = [[0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500],
                    [0.0, 10.9, 21.8, 32.7, 43.6, 54.5, 65.4, 76.3, 87.2, 98.1, 109.0, 119.8, 130.7, 141.6]]
        result = Calculate.JeepGearSplitter.calculateSpeedFromRpm(jeep_model='jk',
                                                                  differentialGearRatio=4.56,
                                                                  tireDiameter=33.4,
                                                                  gearSelected=4,
                                                                  transmissionType='automatic',
                                                                  rubicon=False,
                                                                  fourLowEngaged=False)
        print(result)
        self.assertEqual(result, expected)

    #### JL ####
    def test_6thGear_noTransferCase_For_Rpm(self):
        expected = [[0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500],
                    [0.0, 10.9, 21.8, 32.7, 43.6, 54.5, 65.4, 76.3, 87.2, 98.1, 109.0, 119.8, 130.7, 141.6]]
        result = Calculate.JeepGearSplitter.calculateSpeedFromRpm(jeep_model='jl',
                                                                  differentialGearRatio=4.56,
                                                                  tireDiameter=33.4,
                                                                  gearSelected=6,
                                                                  transmissionType='automatic',
                                                                  rubicon=True,
                                                                  fourLowEngaged=False)
        print('result: ', result)
        self.assertEqual(result, expected)

    def test_8thGear_noTransferCase_For_Rpm(self):
        expected = [[0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500],
                    [0.0, 16.3, 32.5, 48.8, 65.0, 81.3, 97.6, 113.8, 130.1, 146.4, 162.6, 178.9, 195.1, 211.4]]
        result = Calculate.JeepGearSplitter.calculateSpeedFromRpm(jeep_model='jl',
                                                                  differentialGearRatio=4.56,
                                                                  tireDiameter=33.4,
                                                                  gearSelected=8,
                                                                  transmissionType='automatic',
                                                                  rubicon=True,
                                                                  fourLowEngaged=False)
        print('result: ', result)
        self.assertEqual(result, expected)

    #
    # ############## Calculate for Speed ################
    #
    def test_5thGear_noTransferCase_For_Speed(self):
        expected = [[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115],
                    [0, 190, 380, 571, 761, 952, 1142, 1333, 1523, 1714, 1904, 2094, 2285, 2475, 2666, 2856, 3047, 3237, 3428, 3618, 3808, 3999, 4189, 4380]]
        result = Calculate.JeepGearSplitter.calculateRpmFromSpeed(jeep_model='jk',
                                                                  differentialGearRatio=4.56,
                                                                  tireDiameter=33.4,
                                                                  gearSelected=5,
                                                                  transmissionType='automatic',
                                                                  rubicon=False,
                                                                  fourLowEngaged=False)

        self.assertEqual(result, expected)

    def test_6thGear_noTransferCase_For_Speed_Manual(self):
        expected = [[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115],
                    [0, 182, 365, 548, 731, 914, 1097, 1280, 1463, 1645, 1828, 2011, 2194, 2377, 2560, 2743, 2926, 3108, 3291, 3474, 3657, 3840, 4023, 4206]]
        result = Calculate.JeepGearSplitter.calculateRpmFromSpeed(jeep_model='jk',
                                                                  differentialGearRatio=4.56,
                                                                  tireDiameter=33.4,
                                                                  gearSelected=6,
                                                                  transmissionType='manual',
                                                                  rubicon=False,
                                                                  fourLowEngaged=False)

        self.assertEqual(result, expected)

    def test_6thGear_TransferCase_For_Speed_Manual(self):
        expected = [[0, 5, 10, 15, 20, 25, 30, 35, 40, 45], [0, 731, 1463, 2194, 2926, 3657, 4389, 5120, 5852, 6583]]
        result = Calculate.JeepGearSplitter.calculateRpmFromSpeed(jeep_model='jk',
                                                                  differentialGearRatio=4.56,
                                                                  tireDiameter=33.4,
                                                                  gearSelected=6,
                                                                  transmissionType='manual',
                                                                  rubicon=True,
                                                                  fourLowEngaged=True)

        self.assertEqual(result, expected)

    def test_5thGear_TransferCase_For_Speed_Auto(self):
        expected = [[0, 5, 10, 15, 20, 25, 30, 35, 40, 45], [0, 761, 1523, 2285, 3047, 3808, 4570, 5332, 6094, 6856]]
        result = Calculate.JeepGearSplitter.calculateRpmFromSpeed(jeep_model='jk',
                                                                  differentialGearRatio=4.56,
                                                                  tireDiameter=33.4,
                                                                  gearSelected=5,
                                                                  transmissionType='automatic',
                                                                  rubicon=True,
                                                                  fourLowEngaged=True)

        self.assertEqual(result, expected)
