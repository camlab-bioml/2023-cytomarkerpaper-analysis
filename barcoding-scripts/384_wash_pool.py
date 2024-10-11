from opentrons import types
import math

metadata = {
    'protocolName': 'Barcode Wash Pool 384',
    'author': 'RC',
    'source': 'McGuigan Lab',
    'apiLevel': '2.11'
    }

def run(ctx):

    # 0) load instrument
    tipracks_1 = ctx.load_labware('opentrons_96_tiprack_300ul', '1') #20ul tips
    tipracks_2 = ctx.load_labware('opentrons_96_tiprack_300ul', '3') #20ul tips
    tipracks_3 = ctx.load_labware('opentrons_96_tiprack_300ul', '4') #20ul tips
    tipracks_4 = ctx.load_labware('opentrons_96_tiprack_300ul', '6') #20ul tips
    tip_racks=[tipracks_1,tipracks_2,tipracks_3,tipracks_4]
    left_pip = ctx.load_instrument('p20_multi_gen2', 'left')
    right_pip = ctx.load_instrument('p300_multi_gen2', 'right', tip_racks=[tipracks_1,tipracks_2,tipracks_3,tipracks_4]) #p300_multi
    
    source_cells = ctx.load_labware('corning_384_wellplate_112ul_flat', '2')
    
    washing_1 = ctx.load_labware("nest_96_wellplate_2ml_deep", '7')
    washing_2 = ctx.load_labware("nest_96_wellplate_2ml_deep", '8')
    washing_3 = ctx.load_labware("nest_96_wellplate_2ml_deep", '9')
    washing_4 = ctx.load_labware("nest_96_wellplate_2ml_deep", '11')
    washing = [washing_1,washing_2,washing_3,washing_4]
    
    trash = ctx.load_labware("axygen_1_reservoir_90ml", '5')
    reservior = ctx.load_labware("axygen_1_reservoir_90ml", '10')

    columns = ['A1','B1','A2','B2','A3','B3','A4','B4','A5','B5','A6','B6','A7','B7','A8','B8','A9','B9','A10','B10','A11','B11','A12','B12','A13','B13','A14','B14','A15','B15','A16','B16','A17','B17','A18','B18','A19','B19','A20','B20','A21','B21','A22','B22','A23','B23','A24','B24']
    wash_well = ["A1", "A2", "A3", "A4", "A5", "A6", "A7","A8","A9","A10","A11","A12"]
    
      
    #Remove supernatant and add more PBS-BSA
    j = 0
    k = 0
    for i in range(len(columns)): 
        right_pip.pick_up_tip(tip_racks[j][wash_well[k]])
        right_pip.aspirate(50, source_cells[columns[i]].bottom(z=3),0.1)
        right_pip.dispense(50, trash.rows()[0][0],3)
        right_pip.aspirate(60, washing[j][wash_well[k]].bottom())
        right_pip.dispense(60, source_cells[columns[i]].bottom(z=2))
        right_pip.mix(3, 50, source_cells[columns[i]].bottom(z=2))
        right_pip.touch_tip()
        right_pip.return_tip()
        if k < 11:
            k += 1
        else:
            j += 1
            k = 0
     
    ctx.pause("Spin # 2")
    
    #Remove supernatant and add more PBS-BSA
    j = 0
    k = 0
    for i in range(len(columns)): 
        right_pip.pick_up_tip(tip_racks[j][wash_well[k]])
        right_pip.aspirate(60, source_cells[columns[i]].bottom(z=3),0.1)
        right_pip.dispense(60, trash.rows()[0][0],3)
        right_pip.aspirate(60, washing[j][wash_well[k]].bottom())
        right_pip.dispense(60, source_cells[columns[i]].bottom(z=2))
        right_pip.mix(3, 50, source_cells[columns[i]].bottom(z=2))
        right_pip.touch_tip()
        right_pip.return_tip()
        if k < 11:
            k += 1
        else:
            j += 1
            k = 0
        
        
    ctx.pause("Spin # 3")
    
    #Remove supernatant and add more PBS-BSA and collect all cell suspension
    j = 0
    k = 0
    for i in range(len(columns)): 
        right_pip.pick_up_tip(tip_racks[j][wash_well[k]])
        right_pip.aspirate(60, source_cells[columns[i]].bottom(z=3),0.1)
        right_pip.dispense(60, trash.rows()[0][0],3)
        right_pip.aspirate(60, washing[j][wash_well[k]].bottom())
        right_pip.dispense(60, source_cells[columns[i]].bottom(z=2))
        right_pip.mix(3, 50, source_cells[columns[i]].bottom(z=2))
        right_pip.aspirate(90, source_cells[columns[i]].bottom(z=0.8))
        right_pip.dispense(90, reservior['A1'],3)
        right_pip.aspirate(80, washing[j][wash_well[k]].bottom())
        right_pip.dispense(80, source_cells[columns[i]].bottom(z=2))
        right_pip.mix(3, 50, source_cells[columns[i]].bottom(z=2))
        right_pip.aspirate(90, source_cells[columns[i]].bottom(z=0.8))
        right_pip.dispense(90, reservior['A1'],3)
        right_pip.drop_tip()
        if k < 11:
            k += 1
        else:
            j += 1
            k = 0
        

