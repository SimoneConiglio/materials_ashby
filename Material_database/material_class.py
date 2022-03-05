"""Define the material class"""
import plotly.graph_objects as go
import plotly.offline as pyo
from pandas import DataFrame, concat


class MaterialProperty():
    def __init__(self, name, units=None, kind=None):
        self.name = name
        self.units = units
        self.lb = None
        self.ub = None
        self.value = None
        self.dispersion = None
        self.kind = kind

    def update(self, lb=None, ub=None, value=None):
        if lb is None:
            lb = value
        if ub is None:
            ub = value
        if value is None and self.kind == float:
            value = (lb + ub) / 2.
        self.lb = lb
        self.ub = ub
        self.value = value
        if self.kind == float:
            self.dispersion = ub - value


class Material():
    def __init__(self, name, composition=None):
        self.name = name
        self.composition = composition
        self.price = MaterialProperty(name="Price", units="USD/kg", kind=float)
        self.density = MaterialProperty(name="Density", units="kg/m3", kind=float)
        self.young_modulus = MaterialProperty(name="Young's modulus", units="GPa", kind=float)
        self.yield_strength = MaterialProperty(name="Elastic limit", units="MPa", kind=float)
        self.tensile_strength = MaterialProperty(name="Tensile strength", units="MPa", kind=float)
        self.elongation = MaterialProperty(name="Elongation", units="%", kind=float)
        self.hardness_vickers = MaterialProperty(name="Hardness Vickers", units="HV", kind=float)
        self.fatigue_strength = MaterialProperty(name="Fatigue limit", units="MPa", kind=float)
        self.fracture_toughness = MaterialProperty(name="Fracture toughness", units="MPam1/2", kind=float)
        self.melting_point = MaterialProperty(name="Melting point", units="°C", kind=float)
        self.maximum_service_temperature = MaterialProperty(name="Maximum service temperature", units="°C", kind=float)
        self.thermal_conductivity = MaterialProperty(name="Thermal conductivity", units="W/mK", kind=float)
        self.specific_heat_capacity = MaterialProperty(name="Specific heat capacity", units="J/kgK", kind=float)
        self.thermal_expansion_coefficient = MaterialProperty(name="Thermal expansion coefficient", units="10-6/°C",
                                                              kind=float)
        self.electrical_resistivity = MaterialProperty(name="Electrical resistivity", units="10-6 Ohm cm", kind=float)
        self.global_production = MaterialProperty(name="Global production", units="t/yr", kind=float)
        self.reserves = MaterialProperty(name="Reserves", units="t", kind=float)
        self.embodied_energy_primary_production = MaterialProperty(name="Embodied energy, primary production",
                                                                   units="MJ/Kg", kind=float)
        self.co2_footprint_primary_production = MaterialProperty(name="CO2 footprint, primary production",
                                                                 units="Kg/Kg",
                                                                 kind=float)
        self.water_usage = MaterialProperty(name="Water usage", units="l/Kg", kind=float)
        self.eco_indicator = MaterialProperty(name="Eco-indicator", units="millipoints/Kg", kind=float)
        self.casting_energy = MaterialProperty(name="Casting Energy", units="MJ/Kg", kind=float)
        self.casting_co2_footprint = MaterialProperty(name="Casting CO2 footprint", units="Kg/Kg", kind=float)
        self.deformation_energy = MaterialProperty(name="Deformation Energy", units="MJ/Kg", kind=float)
        self.deformation_co2_footprint = MaterialProperty(name="Deformation CO2 footprint", units="Kg/Kg", kind=float)
        self.embodied_energy_recycling = MaterialProperty(name="Embodied energy recycling", units="MJ/Kg", kind=float)
        self.co2_footprint_recycling = MaterialProperty(name="CO2 footprint, recycling", units="Kg/Kg", kind=float)
        self.recycle_fraction = MaterialProperty(name="Recycle fraction", units="%", kind=float)

    def get_pandas_dataframe(self):
        my_dict = {}
        for attribute_name, value in vars(self).items():
            if isinstance(value, MaterialProperty):
                my_dict[attribute_name] = vars(value)
            else:
                my_dict[attribute_name] = value
        return DataFrame(my_dict)


if __name__ == '__main__':
    material_list = []
    # Low Carbon Steel
    low_carbon_steel = Material(name="Low carbon steel", composition="Fe/0.02-0.3C")
    low_carbon_steel.density.update(lb=7800., ub=7900.)
    low_carbon_steel.price.update(lb=.68, ub=.74)
    low_carbon_steel.young_modulus.update(lb=200., ub=215.)
    low_carbon_steel.yield_strength.update(lb=250., ub=395.)
    low_carbon_steel.tensile_strength.update(lb=345., ub=580.)
    low_carbon_steel.elongation.update(lb=26., ub=47.)
    low_carbon_steel.hardness_vickers.update(lb=107., ub=172.)
    low_carbon_steel.fatigue_strength.update(lb=203., ub=293.)
    low_carbon_steel.fracture_toughness.update(lb=41., ub=82.)
    low_carbon_steel.melting_point.update(lb=1480., ub=1530.)
    low_carbon_steel.maximum_service_temperature.update(lb=350., ub=400.)
    low_carbon_steel.thermal_conductivity.update(lb=49., ub=54.)
    low_carbon_steel.specific_heat_capacity.update(lb=460., ub=505.)
    low_carbon_steel.thermal_expansion_coefficient.update(lb=11.5, ub=13.)
    low_carbon_steel.electrical_resistivity.update(lb=15., ub=20.)
    low_carbon_steel.global_production.update(value=2.3 * 10 ** 9)
    low_carbon_steel.reserves.update(value=160 * 10 ** 9)
    low_carbon_steel.embodied_energy_primary_production.update(lb=25., ub=28.)
    low_carbon_steel.co2_footprint_primary_production.update(lb=1.7, ub=1.9)
    low_carbon_steel.water_usage.update(lb=23., ub=69.)
    low_carbon_steel.eco_indicator.update(value=106.)
    low_carbon_steel.casting_energy.update(lb=11., ub=12.2)
    low_carbon_steel.casting_co2_footprint.update(lb=0.8, ub=0.9)
    low_carbon_steel.deformation_energy.update(lb=3., ub=6.)
    low_carbon_steel.deformation_co2_footprint.update(lb=0.22, ub=0.46)
    low_carbon_steel.embodied_energy_recycling.update(lb=6.6, ub=8.)
    low_carbon_steel.co2_footprint_recycling.update(lb=0.4, ub=.48)
    low_carbon_steel.recycle_fraction.update(lb=40., ub=44.)
    material_list.append(low_carbon_steel)
    # low alloy steel
    low_alloy_steel = Material(name="Low alloy steel", composition="Fe/1.0 C/<2.5 Cr/<2.5 Ni/<2.5Mo/<2.5 V")
    low_alloy_steel.density.update(lb=7800., ub=7900.)
    low_alloy_steel.price.update(lb=.9, ub=1.1)
    low_alloy_steel.young_modulus.update(lb=205., ub=217.)
    low_alloy_steel.yield_strength.update(lb=400., ub=1500.)
    low_alloy_steel.tensile_strength.update(lb=550., ub=1760.)
    low_alloy_steel.elongation.update(lb=3., ub=38.)
    low_alloy_steel.hardness_vickers.update(lb=140., ub=692.)
    low_alloy_steel.fatigue_strength.update(lb=248., ub=700.)
    low_alloy_steel.fracture_toughness.update(lb=14., ub=200.)
    low_alloy_steel.melting_point.update(lb=1380., ub=1530.)
    low_alloy_steel.maximum_service_temperature.update(lb=500., ub=530.)
    low_alloy_steel.thermal_conductivity.update(lb=34., ub=55.)
    low_alloy_steel.specific_heat_capacity.update(lb=410., ub=530.)
    low_alloy_steel.thermal_expansion_coefficient.update(lb=10.5, ub=13.5)
    low_alloy_steel.electrical_resistivity.update(lb=15., ub=35.)
    low_alloy_steel.global_production.update(value=2.3 * 10 ** 9)
    low_alloy_steel.reserves.update(value=159 * 10 ** 9)
    low_alloy_steel.embodied_energy_primary_production.update(lb=31., ub=34.)
    low_alloy_steel.co2_footprint_primary_production.update(lb=1.9, ub=2.1)
    low_alloy_steel.water_usage.update(lb=37., ub=111.)
    low_alloy_steel.eco_indicator.update(value=200.)
    low_alloy_steel.casting_energy.update(lb=10.9, ub=12.)
    low_alloy_steel.casting_co2_footprint.update(lb=0.8, ub=0.9)
    low_alloy_steel.deformation_energy.update(lb=7., ub=14.)
    low_alloy_steel.deformation_co2_footprint.update(lb=0.5, ub=1.1)
    low_alloy_steel.embodied_energy_recycling.update(lb=7.7, ub=9.5)
    low_alloy_steel.co2_footprint_recycling.update(lb=0.47, ub=.57)
    low_alloy_steel.recycle_fraction.update(lb=40., ub=44.)
    material_list.append(low_alloy_steel)
    # stainless steel
    stainless_steel = Material(name="Stainless steel", composition="Fe/0.25 C/<16-30 Cr/3.5 - 37 Ni/<10 Mo + Si,P,S,N")
    stainless_steel.density.update(lb=7600., ub=8100.)
    stainless_steel.price.update(lb=8.2, ub=9.1)
    stainless_steel.young_modulus.update(lb=189., ub=210.)
    stainless_steel.yield_strength.update(lb=170., ub=1000.)
    stainless_steel.tensile_strength.update(lb=480., ub=2240.)
    stainless_steel.elongation.update(lb=5., ub=70.)
    stainless_steel.hardness_vickers.update(lb=130., ub=570.)
    stainless_steel.fatigue_strength.update(lb=175., ub=753.)
    stainless_steel.fracture_toughness.update(lb=62., ub=150.)
    stainless_steel.melting_point.update(lb=1370., ub=1450.)
    stainless_steel.maximum_service_temperature.update(lb=750., ub=820.)
    stainless_steel.thermal_conductivity.update(lb=12., ub=24.)
    stainless_steel.specific_heat_capacity.update(lb=450., ub=530.)
    stainless_steel.thermal_expansion_coefficient.update(lb=13, ub=20)
    stainless_steel.electrical_resistivity.update(lb=64., ub=107.)
    stainless_steel.global_production.update(value=30 * 10 ** 6)
    stainless_steel.reserves.update(value=2.5 * 10 ** 9)
    stainless_steel.embodied_energy_primary_production.update(lb=81., ub=88.)
    stainless_steel.co2_footprint_primary_production.update(lb=4.7, ub=5.2)
    stainless_steel.water_usage.update(lb=112., ub=336.)
    stainless_steel.eco_indicator.update(value=310.)
    stainless_steel.casting_energy.update(lb=10., ub=12.)
    stainless_steel.casting_co2_footprint.update(lb=0.8, ub=0.9)
    stainless_steel.deformation_energy.update(lb=5., ub=11.4)
    stainless_steel.deformation_co2_footprint.update(lb=0.4, ub=0.8)
    stainless_steel.embodied_energy_recycling.update(lb=11., ub=13.)
    stainless_steel.co2_footprint_recycling.update(lb=0.65, ub=.8)
    stainless_steel.recycle_fraction.update(lb=35., ub=40.)
    material_list.append(stainless_steel)
    # Cast iron, ductile (nodular)
    cast_iron = Material(name="Cast iron, ductile (nodular)",
                         composition="Fe/3.2-4.1%C/1.8-2.8% Si/<0.8% Mn/<0.1% P/<0.03% S")
    cast_iron.density.update(lb=7050., ub=7250.)
    cast_iron.price.update(lb=0.5, ub=0.65)
    cast_iron.young_modulus.update(lb=165., ub=180.)
    cast_iron.yield_strength.update(lb=250., ub=680.)
    cast_iron.tensile_strength.update(lb=410., ub=830.)
    cast_iron.elongation.update(lb=3., ub=18.)
    cast_iron.hardness_vickers.update(lb=115., ub=320.)
    cast_iron.fatigue_strength.update(lb=180., ub=330.)
    cast_iron.fracture_toughness.update(lb=22., ub=54.)
    cast_iron.melting_point.update(lb=1130., ub=1250.)
    cast_iron.maximum_service_temperature.update(lb=350., ub=745.)
    cast_iron.thermal_conductivity.update(lb=29., ub=44.)
    cast_iron.specific_heat_capacity.update(lb=460., ub=495.)
    cast_iron.thermal_expansion_coefficient.update(lb=10, ub=12.5)
    cast_iron.electrical_resistivity.update(lb=49., ub=56.)
    cast_iron.global_production.update(value=2.3 * 10 ** 9)
    cast_iron.reserves.update(value=159 * 10 ** 9)
    cast_iron.embodied_energy_primary_production.update(lb=16., ub=20.)
    cast_iron.co2_footprint_primary_production.update(lb=1.4, ub=1.6)
    cast_iron.water_usage.update(lb=13., ub=39.)
    cast_iron.eco_indicator.update(value=80.)
    cast_iron.casting_energy.update(lb=10., ub=11.)
    cast_iron.casting_co2_footprint.update(lb=0.75, ub=0.83)
    cast_iron.embodied_energy_recycling.update(lb=10., ub=11.)
    cast_iron.co2_footprint_recycling.update(lb=0.48, ub=.55)
    cast_iron.recycle_fraction.update(lb=66., ub=72.)
    material_list.append(cast_iron)
    # Aluminum alloys
    aluminium_alloys = Material(name="Aluminium alloys",
                                composition="Al + Mg, Mn, Cr, Cu, Zn, Zr, Li")
    aluminium_alloys.density.update(lb=2500., ub=2900.)
    aluminium_alloys.price.update(lb=2.4, ub=2.7)
    aluminium_alloys.young_modulus.update(lb=68., ub=82.)
    aluminium_alloys.yield_strength.update(lb=30., ub=550.)
    aluminium_alloys.tensile_strength.update(lb=58., ub=550.)
    aluminium_alloys.elongation.update(lb=1., ub=44.)
    aluminium_alloys.hardness_vickers.update(lb=12., ub=150.)
    aluminium_alloys.fatigue_strength.update(lb=22., ub=160.)
    aluminium_alloys.fracture_toughness.update(lb=22., ub=35.)
    aluminium_alloys.melting_point.update(lb=495., ub=640.)
    aluminium_alloys.maximum_service_temperature.update(lb=120., ub=200.)
    aluminium_alloys.thermal_conductivity.update(lb=76., ub=240.)
    aluminium_alloys.specific_heat_capacity.update(lb=860., ub=990.)
    aluminium_alloys.thermal_expansion_coefficient.update(lb=21., ub=24.)
    aluminium_alloys.electrical_resistivity.update(lb=2.5, ub=6.)
    aluminium_alloys.global_production.update(value=37. * 10 ** 6)
    aluminium_alloys.reserves.update(value=2 * 10 ** 9)
    aluminium_alloys.embodied_energy_primary_production.update(lb=200., ub=220.)
    aluminium_alloys.co2_footprint_primary_production.update(lb=11., ub=13.)
    aluminium_alloys.water_usage.update(lb=495., ub=1490.)
    aluminium_alloys.eco_indicator.update(value=710.)
    aluminium_alloys.casting_energy.update(lb=11., ub=12.2)
    aluminium_alloys.casting_co2_footprint.update(lb=0.82, ub=0.91)
    aluminium_alloys.deformation_energy.update(lb=3.3, ub=6.8)
    aluminium_alloys.deformation_co2_footprint.update(lb=0.19, ub=0.23)
    aluminium_alloys.embodied_energy_recycling.update(lb=22., ub=30.)
    aluminium_alloys.co2_footprint_recycling.update(lb=1.9, ub=2.3)
    aluminium_alloys.recycle_fraction.update(lb=41., ub=45.)
    material_list.append(aluminium_alloys)
    # Magnesium alloys
    magnesium_alloys = Material(name="Magnesium alloys",
                                composition="Mg + Al, Mn, Si, Zn, Cu, Li, rare elements")
    magnesium_alloys.density.update(lb=1740., ub=1950.)
    magnesium_alloys.price.update(lb=4.7, ub=5.1)
    magnesium_alloys.young_modulus.update(lb=42., ub=47.)
    magnesium_alloys.yield_strength.update(lb=70., ub=400.)
    magnesium_alloys.tensile_strength.update(lb=185., ub=475.)
    magnesium_alloys.elongation.update(lb=3.5, ub=18.)
    magnesium_alloys.hardness_vickers.update(lb=35., ub=135.)
    magnesium_alloys.fatigue_strength.update(lb=60., ub=225.)
    magnesium_alloys.fracture_toughness.update(lb=12., ub=18.)
    magnesium_alloys.melting_point.update(lb=447., ub=649.)
    magnesium_alloys.maximum_service_temperature.update(lb=120., ub=200.)
    magnesium_alloys.thermal_conductivity.update(lb=50., ub=156.)
    magnesium_alloys.specific_heat_capacity.update(lb=955., ub=1060.)
    magnesium_alloys.thermal_expansion_coefficient.update(lb=24.6, ub=28.)
    magnesium_alloys.electrical_resistivity.update(lb=4.15, ub=15.)
    magnesium_alloys.global_production.update(value=0.6 * 10 ** 6)
    magnesium_alloys.reserves.update(value=1 * 10 ** 9)
    magnesium_alloys.embodied_energy_primary_production.update(lb=300., ub=330.)
    magnesium_alloys.co2_footprint_primary_production.update(lb=34., ub=38.)
    magnesium_alloys.water_usage.update(lb=500., ub=1500.)
    magnesium_alloys.eco_indicator.update(value=1500.)
    magnesium_alloys.casting_energy.update(lb=11.1, ub=12.3)
    magnesium_alloys.casting_co2_footprint.update(lb=0.83, ub=0.92)
    magnesium_alloys.deformation_energy.update(lb=3.8, ub=6.6)
    magnesium_alloys.deformation_co2_footprint.update(lb=0.3, ub=0.5)
    magnesium_alloys.embodied_energy_recycling.update(lb=23., ub=26.)
    magnesium_alloys.co2_footprint_recycling.update(lb=2.6, ub=3.2)
    magnesium_alloys.recycle_fraction.update(lb=36., ub=41.)
    material_list.append(magnesium_alloys)
    # Titanium alloys
    titanium_alloys = Material(name="Titanium alloys",
                               composition="Ti + Al, Zr, Cr, Mo, Si, Sn, Ni, Fe, V")
    titanium_alloys.density.update(lb=4400., ub=4800.)
    titanium_alloys.price.update(lb=57., ub=63.)
    titanium_alloys.young_modulus.update(lb=110., ub=120.)
    titanium_alloys.yield_strength.update(lb=750., ub=1200.)
    titanium_alloys.tensile_strength.update(lb=800., ub=1450.)
    titanium_alloys.elongation.update(lb=5., ub=10.)
    titanium_alloys.hardness_vickers.update(lb=267., ub=380.)
    titanium_alloys.fatigue_strength.update(lb=589., ub=617.)
    titanium_alloys.fracture_toughness.update(lb=55., ub=70.)
    titanium_alloys.melting_point.update(lb=1480., ub=1680.)
    titanium_alloys.maximum_service_temperature.update(lb=450., ub=500.)
    titanium_alloys.thermal_conductivity.update(lb=7., ub=14.)
    titanium_alloys.specific_heat_capacity.update(lb=645., ub=655.)
    titanium_alloys.thermal_expansion_coefficient.update(lb=8.9, ub=9.6)
    titanium_alloys.electrical_resistivity.update(lb=100., ub=170.)
    titanium_alloys.global_production.update(value=0.2 * 10 ** 6)
    titanium_alloys.reserves.update(value=720 * 10 ** 6)
    titanium_alloys.embodied_energy_primary_production.update(lb=650, ub=720.)
    titanium_alloys.co2_footprint_primary_production.update(lb=44., ub=49.)
    titanium_alloys.water_usage.update(lb=470., ub=1410.)
    titanium_alloys.eco_indicator.update(value=3450.)
    titanium_alloys.casting_energy.update(lb=12.6, ub=13.9)
    titanium_alloys.casting_co2_footprint.update(lb=0.9, ub=1.)
    titanium_alloys.deformation_energy.update(lb=14., ub=15.)
    titanium_alloys.deformation_co2_footprint.update(lb=1.1, ub=1.2)
    titanium_alloys.embodied_energy_recycling.update(lb=78., ub=96.)
    titanium_alloys.co2_footprint_recycling.update(lb=4.7, ub=5.7)
    titanium_alloys.recycle_fraction.update(lb=21., ub=24.)
    material_list.append(titanium_alloys)
    # Nickel-chromium alloys
    nikel_cromium_alloys = Material(name="Nickel-chromium alloys",
                                    composition="Ni+ 10 to 30% Cr+ 0 to 10% Fe")
    nikel_cromium_alloys.density.update(lb=8300., ub=8500.)
    nikel_cromium_alloys.price.update(lb=33., ub=36.)
    nikel_cromium_alloys.young_modulus.update(lb=200., ub=220.)
    nikel_cromium_alloys.yield_strength.update(lb=365., ub=460.)
    nikel_cromium_alloys.tensile_strength.update(lb=615., ub=760.)
    nikel_cromium_alloys.elongation.update(lb=20., ub=35.)
    nikel_cromium_alloys.hardness_vickers.update(lb=160., ub=200.)
    nikel_cromium_alloys.fatigue_strength.update(lb=245., ub=380.)
    nikel_cromium_alloys.fracture_toughness.update(lb=80., ub=110.)
    nikel_cromium_alloys.melting_point.update(lb=1350., ub=1430.)
    nikel_cromium_alloys.maximum_service_temperature.update(lb=900., ub=1000.)
    nikel_cromium_alloys.thermal_conductivity.update(lb=9., ub=15.)
    nikel_cromium_alloys.specific_heat_capacity.update(lb=430., ub=450.)
    nikel_cromium_alloys.thermal_expansion_coefficient.update(lb=12., ub=14.)
    nikel_cromium_alloys.electrical_resistivity.update(lb=102., ub=114.)
    nikel_cromium_alloys.global_production.update(value=1.5 * 10 ** 6)
    nikel_cromium_alloys.reserves.update(value=63 * 10 ** 6)
    nikel_cromium_alloys.embodied_energy_primary_production.update(lb=173., ub=190.)
    nikel_cromium_alloys.co2_footprint_primary_production.update(lb=11., ub=12.)
    nikel_cromium_alloys.water_usage.update(lb=564., ub=620.)
    nikel_cromium_alloys.eco_indicator.update(value=2800.)
    nikel_cromium_alloys.casting_energy.update(lb=10.4, ub=11.5)
    nikel_cromium_alloys.casting_co2_footprint.update(lb=0.78, ub=0.85)
    nikel_cromium_alloys.deformation_energy.update(lb=3.3, ub=6.5)
    nikel_cromium_alloys.deformation_co2_footprint.update(lb=0.25, ub=0.53)
    nikel_cromium_alloys.embodied_energy_recycling.update(lb=30., ub=36.)
    nikel_cromium_alloys.co2_footprint_recycling.update(lb=1.8, ub=2.2)
    nikel_cromium_alloys.recycle_fraction.update(lb=29., ub=32.)
    material_list.append(nikel_cromium_alloys)
    # Nickel-based super alloys
    nikel_super_alloys = Material(name="Nickel-based super alloys",
                                  composition="Ni+ 10 to 25% Cr+ Ti,Al,Co,Mo,Zr,B,Fe")
    nikel_super_alloys.density.update(lb=7750., ub=8650.)
    nikel_super_alloys.price.update(lb=31., ub=33.)
    nikel_super_alloys.young_modulus.update(lb=150., ub=245.)
    nikel_super_alloys.yield_strength.update(lb=300., ub=1900.)
    nikel_super_alloys.tensile_strength.update(lb=400., ub=2100.)
    nikel_super_alloys.elongation.update(lb=0.5, ub=60.)
    nikel_super_alloys.hardness_vickers.update(lb=200., ub=600.)
    nikel_super_alloys.fatigue_strength.update(lb=135., ub=900.)
    nikel_super_alloys.fracture_toughness.update(lb=65., ub=110.)
    nikel_super_alloys.melting_point.update(lb=1280., ub=1410.)
    nikel_super_alloys.maximum_service_temperature.update(lb=900., ub=1200.)
    nikel_super_alloys.thermal_conductivity.update(lb=8., ub=17.)
    nikel_super_alloys.specific_heat_capacity.update(lb=380., ub=490.)
    nikel_super_alloys.thermal_expansion_coefficient.update(lb=9., ub=16.)
    nikel_super_alloys.electrical_resistivity.update(lb=84., ub=240.)
    nikel_super_alloys.global_production.update(value=1.5 * 10 ** 6)
    nikel_super_alloys.reserves.update(value=7 * 10 ** 7)
    nikel_super_alloys.embodied_energy_primary_production.update(lb=221., ub=244.)
    nikel_super_alloys.co2_footprint_primary_production.update(lb=11., ub=12.1)
    nikel_super_alloys.water_usage.update(lb=134., ub=484.)
    nikel_super_alloys.eco_indicator.update(value=2830.)
    nikel_super_alloys.casting_energy.update(lb=10., ub=11.)
    nikel_super_alloys.casting_co2_footprint.update(lb=0.75, ub=0.8)
    nikel_super_alloys.deformation_energy.update(lb=4.2, ub=4.5)
    nikel_super_alloys.deformation_co2_footprint.update(lb=0.31, ub=0.34)
    nikel_super_alloys.embodied_energy_recycling.update(lb=33.8, ub=37.5)
    nikel_super_alloys.co2_footprint_recycling.update(lb=1.97, ub=2.3)
    nikel_super_alloys.recycle_fraction.update(lb=22., ub=26.)
    material_list.append(nikel_super_alloys)
    df_list = []
    for mat in material_list:
        df_list.append(mat.get_pandas_dataframe())
    df = concat(df_list)
    df.to_excel("Material.xlsx")
    selected = df.loc["value", :].drop("composition", axis=1)
    selected.iloc[:, 1:] = (selected.iloc[:, 1:] - selected.iloc[:, 1:].min()) / (
            selected.iloc[:, 1:].max() - selected.iloc[:, 1:].min()) + 0.1
    fig = go.Figure(data=[
        go.Scatterpolar(r=selected.iloc[ind, 1:], theta=selected.columns[1:], fill='toself',
                        name=selected.loc[:, "name"].tolist()[ind]) for ind in
        range(len(selected.loc[:, "name"].tolist()))],
        layout=go.Layout(
            title=go.layout.Title(text='Material comparison'),
            polar={'radialaxis': {'visible': True}},
            showlegend=True))

    pyo.plot(fig)

    df.head()
