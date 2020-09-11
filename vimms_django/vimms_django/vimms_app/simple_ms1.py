from vimms.DataGenerator import extract_hmdb_metabolite, get_data_source
from vimms.DataGenerator import get_spectral_feature_database
from vimms.MassSpec import IndependentMassSpectrometer
from vimms.Controller import SimpleMs1Controller
from vimms.Common import *
from vimms.Roi import make_roi, RoiToChemicalCreator
from vimms.FeatureExtraction import extract_roi


def simple_ms1_processor():
    ''