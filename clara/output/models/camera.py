
from CATAP.common.machine.pv_utils import StatisticalPV, BinaryPV, ScalarPV, WaveformPV, StringPV, StatePV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
import os
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class CameraPVMapModel(PVMap):
    
    
    ANA_AvgIntensity_RBV: StatisticalPV
    
    """Gets the average intensity readback for a camera."""
    
    
    ANA_CPU_CropSubMask_RBV: StatisticalPV
    
    """Crop, subtract and mask CPU."""
    
    
    ANA_CPU_Dot_RBV: StatisticalPV
    
    """Dot product CPU mSecs."""
    
    
    ANA_CPU_Npoint_RBV: StatisticalPV
    
    """N-point CPU mSecs."""
    
    
    ANA_CPU_RBV: StatisticalPV
    
    """Total CPU mSecs."""
    
    
    ANA_CenterX: StatisticalPV
    
    """Camera centre X position."""
    
    
    ANA_CenterX_RBV: StatisticalPV
    
    """Camera centre X position readback."""
    
    
    ANA_CenterY: StatisticalPV
    
    """Camera centre Y position."""
    
    
    ANA_CenterY_RBV: StatisticalPV
    
    """Camera centre Y position readback."""
    
    
    ANA_CovXYPix_RBV: StatisticalPV
    
    """X-Y covariance in pixels."""
    
    
    ANA_CovXY_RBV: StatisticalPV
    
    """X-Y covariance in pixels (readback)."""
    
    
    ANA_EnableCallbacks: BinaryPV
    
    """Enable writing of analysis PVs (readback)."""
    
    
    ANA_EnableCallbacks_RBV: BinaryPV
    
    """Enable writing of analysis PVs (readback)."""
    
    
    ANA_FloorLevel: ScalarPV
    
    """Floor level (pixels) set value."""
    
    
    ANA_FloorLevel_RBV: ScalarPV
    
    """Floor level (pixels) read value."""
    
    
    ANA_FlooredPercent_RBV: ScalarPV
    
    """Floor level (percent) read value."""
    
    
    ANA_FlooredPoints_RBV: ScalarPV
    
    """Floor level (points) read value."""
    
    
    ANA_Intensity_RBV: StatisticalPV
    
    """Camera intensity readback."""
    
    
    ANA_MMResults_RBV: WaveformPV
    
    """Analysis results readback."""
    
    
    ANA_MaskHeight_RBV: ScalarPV
    
    """Height of mask (pixels)."""
    
    
    ANA_MaskWidth_RBV: ScalarPV
    
    """Width of mask (pixels)."""
    
    
    ANA_MaskXCenter: ScalarPV
    
    """Mask vertical centre (pixels)."""
    
    
    ANA_MaskXCenter_RBV: ScalarPV
    
    """Mask horizontal centre (pixels) readback."""
    
    
    ANA_MaskXRad: ScalarPV
    
    """Mask horizontal radius (pixels)."""
    
    
    ANA_MaskXRad_RBV: ScalarPV
    
    """Mask horizontal radius (pixels) readback"""
    
    
    ANA_MaskYCenter: ScalarPV
    
    """Mask vertical centre (pixels)."""
    
    
    ANA_MaskYCenter_RBV: ScalarPV
    
    """Mask vertical centre (pixels) readback."""
    
    
    ANA_MaskYRad: ScalarPV
    
    """Mask vertical radius (pixels)."""
    
    
    ANA_MaskYRad_RBV: ScalarPV
    
    """Mask vertical radius (pixels) readback"""
    
    
    ANA_NPointStepSize: ScalarPV
    
    """N-point scaling step size"""
    
    
    ANA_NPointStepSize_RBV: ScalarPV
    
    """N-point scaling step size readback"""
    
    
    ANA_NewBkgrnd: ScalarPV
    
    """Collect new background image"""
    
    
    ANA_NewBkgrnd_RBV: ScalarPV
    
    """Status of background image collection"""
    
    
    ANA_OVERLAY_1_CROSS: BinaryPV
    
    """Overlay crosshair"""
    
    
    ANA_OVERLAY_1_CROSS_RBV: BinaryPV
    
    """Overlay crosshair readback"""
    
    
    ANA_OVERLAY_2_RESULT: BinaryPV
    
    """Overlay beam position crosshair"""
    
    
    ANA_OVERLAY_2_RESULT_RBV: BinaryPV
    
    """Overlay beam position crosshair readback"""
    
    
    ANA_OVERLAY_3_MASK: BinaryPV
    
    """Overlay analysis mask"""
    
    
    ANA_OVERLAY_3_MASK_RBV: BinaryPV
    
    """Overlay analysis mask readback"""
    
    
    ANA_PixH_RBV: ScalarPV
    
    """Full image height (pixels)"""
    
    
    ANA_PixMM: ScalarPV
    
    """Pixel-to-mm conversion"""
    
    
    ANA_PixMM_RBV: ScalarPV
    
    """Pixel-to-mm conversion"""
    
    
    ANA_PixW_RBV: ScalarPV
    
    """Full image width (pixels)"""
    
    
    ANA_PixelResults_RBV: WaveformPV
    
    """Image analysis results in pixels"""
    
    
    ANA_SigmaXPix_RBV: StatisticalPV
    
    """Beam horizontal sigma readback value (pixels)"""
    
    
    ANA_SigmaX_RBV: StatisticalPV
    
    """Beam horizontal sigma readback value (mm)"""
    
    
    ANA_SigmaYPix_RBV: StatisticalPV
    
    """Beam vertical sigma readback value (pixels)"""
    
    
    ANA_SigmaY_RBV: StatisticalPV
    
    """Beam vertical sigma readback value (mm)"""
    
    
    ANA_UseBkgrnd: ScalarPV
    
    """Subtract background for display"""
    
    
    ANA_UseBkgrnd_RBV: ScalarPV
    
    """Subtract background for display (readback)"""
    
    
    ANA_UseFloor: ScalarPV
    
    """Use floor for display"""
    
    
    ANA_UseFloor_RBV: ScalarPV
    
    """Use floor for display (readback)"""
    
    
    ANA_UseNPoint: ScalarPV
    
    """Use N-point scaling for display)"""
    
    
    ANA_UseNPoint_RBV: ScalarPV
    
    """Use N-point scaling for display (readback)"""
    
    
    ANA_XPix_RBV: StatisticalPV
    
    """Beam horizontal position (pixels)"""
    
    
    ANA_X_RBV: StatisticalPV
    
    """Beam horizontal position (mm)"""
    
    
    ANA_YPix_RBV: StatisticalPV
    
    """Beam vertical position (pixels)"""
    
    
    ANA_Y_RBV: StatisticalPV
    
    """Beam vertical position (pixels)"""
    
    
    Buffer_Status: StringPV
    
    """Status of buffer saving"""
    
    
    CAM1_ArrayData: WaveformPV
    
    """Full camera image"""
    
    
    CAM2_ArrayData: WaveformPV
    
    """Mask image"""
    
    
    CAM_AcquirePeriod_RBV: ScalarPV
    
    """Image acquisition period"""
    
    
    CAM_AcquireTime_RBV: StatisticalPV
    
    """Image acquisition time"""
    
    
    CAM_Acquire_RBV: BinaryPV
    
    """Camera acquiring state readback"""
    
    
    CAM_Active_Count: ScalarPV
    
    """Not sure"""
    
    
    CAM_Active_Limit: ScalarPV
    
    """Not sure"""
    
    
    CAM_ArrayRate_RBV: StatisticalPV
    
    """Camera acquisition rate"""
    
    
    CAM_Start_Acquire: BinaryPV
    
    """Start camera acquiring"""
    
    
    CAM_Stop_Acquire: BinaryPV
    
    """Stop camera acquiring"""
    
    
    CAM_Temperature_RBV: ScalarPV
    
    """Camera temperature"""
    
    
    HDFB_AutoSave: BinaryPV
    
    """Autosave HDF buffer images."""
    
    
    HDFB_Buffer_FileNumber: ScalarPV
    
    """Not sure"""
    
    
    HDFB_Buffer_FileNumber_RBV: ScalarPV
    
    """Not sure"""
    
    
    HDFB_Capture: BinaryPV
    
    """HDF buffer image capture state"""
    
    
    HDFB_Capture_DISV: BinaryPV
    
    """HDF buffer image capture state"""
    
    
    HDFB_Capture_RBV: BinaryPV
    
    """HDF buffer image capture state (readback)"""
    
    
    HDFB_FileName: StringPV
    
    """Last saved HDF buffer image name"""
    
    
    HDFB_FileName_RBV: StringPV
    
    """Last saved HDF buffer image name readback"""
    
    
    HDFB_FileNumber: ScalarPV
    
    """Not sure"""
    
    
    HDFB_FileNumber_RBV: StatisticalPV
    
    """Not sure"""
    
    
    HDFB_FilePath: StringPV
    
    """File path to claraserv3 buffer image (server path not indicated)"""
    
    
    HDFB_FilePath_RBV: StringPV
    
    """File path to claraserv3 buffer image (server path not indicated)"""
    
    
    HDFB_FileWriteMode: StatePV
    
    """Save mode for HDF buffer images."""
    
    
    HDFB_NumCapture: ScalarPV
    
    """Number of HDF buffer images to collect"""
    
    
    HDFB_NumCapture_RBV: ScalarPV
    
    """Number of HDF buffer images to collect"""
    
    
    HDFB_NumCaptured_RBV: ScalarPV
    
    """Number of buffer images captured"""
    
    
    HDFB_NumImagesCached_RBV: ScalarPV
    
    """Number of buffer images cached"""
    
    
    HDFB_PostCount: ScalarPV
    
    """Post-count number of buffer images"""
    
    
    HDFB_PreCount: ScalarPV
    
    """Pre-count number of buffer images"""
    
    
    HDFB_WriteFile: BinaryPV
    
    """Write HDF buffer file status"""
    
    
    HDFB_WriteFile_RBV: BinaryPV
    
    """Write HDF buffer file status (readback)"""
    
    
    HDFB_WriteMessage: StringPV
    
    """None"""
    
    
    HDFB_WriteStatus: BinaryPV
    
    """Status of writing to HDF buffer"""
    
    
    HDFB_image_buffer_fileName: StringPV
    
    """Image buffer filename"""
    
    
    HDFB_image_buffer_fileName_RBV: StringPV
    
    """Image buffer filename (readback)"""
    
    
    HDFB_image_buffer_filePath: StringPV
    
    """Image buffer file path"""
    
    
    HDFB_image_buffer_filePath_RBV: StringPV
    
    """Image buffer file path (readback)"""
    
    
    HDFB_image_buffer_trigger: ScalarPV
    
    """Trigger image buffer collection"""
    
    
    HDFM_AutoSave: BinaryPV
    
    """Autosave HDF mask images."""
    
    
    HDFM_Capture: BinaryPV
    
    """HDF mask image capture state"""
    
    
    HDFM_Capture_DISV: BinaryPV
    
    """HDF mask image capture state"""
    
    
    HDFM_Capture_RBV: BinaryPV
    
    """HDF mask image capture state (readback)"""
    
    
    HDFM_FileName: StringPV
    
    """Last saved HDF mask image name"""
    
    
    HDFM_FileName_RBV: StringPV
    
    """Last saved HDF mask image name readback"""
    
    
    HDFM_FileNumber: ScalarPV
    
    """Not sure"""
    
    
    HDFM_FileNumber_RBV: StatisticalPV
    
    """Not sure"""
    
    
    HDFM_FilePath: StringPV
    
    """File path to claraserv3 mask image (server path not indicated)"""
    
    
    HDFM_FilePath_RBV: StringPV
    
    """File path to claraserv3 mask image (server path not indicated)"""
    
    
    HDFM_FileWriteMode: StatePV
    
    """Save mode for HDF mask images."""
    
    
    HDFM_NumCapture: ScalarPV
    
    """Number of HDF mask images to collect"""
    
    
    HDFM_NumCapture_RBV: ScalarPV
    
    """Number of HDF mask images to collect"""
    
    
    HDFM_WriteFile: BinaryPV
    
    """Write HDF mask file"""
    
    
    HDFM_WriteFile_RBV: BinaryPV
    
    """None"""
    
    
    HDFM_WriteMessage: StringPV
    
    """None"""
    
    
    HDFM_WriteStatus: BinaryPV
    
    """Status of writing to compressed HDF"""
    
    
    HDF_AutoSave: BinaryPV
    
    """Autosave HDF images."""
    
    
    HDF_Capture: BinaryPV
    
    """HDF image capture state"""
    
    
    HDF_Capture_DISV: BinaryPV
    
    """HDF image capture state"""
    
    
    HDF_Capture_RBV: BinaryPV
    
    """HDF image capture state (readback)"""
    
    
    HDF_FileName: StringPV
    
    """Last saved HDF image name"""
    
    
    HDF_FileName_RBV: StringPV
    
    """Last saved HDF image name readback"""
    
    
    HDF_FileNumber: ScalarPV
    
    """Not sure"""
    
    
    HDF_FileNumber_RBV: StatisticalPV
    
    """Not sure"""
    
    
    HDF_FilePath: StringPV
    
    """File path to claraserv3 (server path not indicated)"""
    
    
    HDF_FilePath_RBV: StringPV
    
    """File path to claraserv3 (server path not indicated)"""
    
    
    HDF_FileWriteMode: StatePV
    
    """Save mode for HDF images."""
    
    
    HDF_NumCapture: ScalarPV
    
    """Number of HDF images to collect"""
    
    
    HDF_NumCapture_RBV: ScalarPV
    
    """Number of HDF images to collect"""
    
    
    HDF_WriteFile: BinaryPV
    
    """Write HDF file"""
    
    
    HDF_WriteFile_RBV: BinaryPV
    
    """HDF file writing status (readback)"""
    
    
    HDF_WriteMessage: StringPV
    
    """Not sure"""
    
    
    HDF_WriteStatus: BinaryPV
    
    """HDF file writing status"""
    
    
    Init_Buffer: BinaryPV
    
    """Initialise image save path"""
    
    
    LED_Off: BinaryPV
    
    """Switch LEDs on"""
    
    
    LED_On: BinaryPV
    
    """Switch LEDs off"""
    
    
    LED_Sta: BinaryPV
    
    """Are LEDs on?"""
    
    
    MAGICK_AutoSave: BinaryPV
    
    """Autosave compressed images."""
    
    
    MAGICK_Capture: BinaryPV
    
    """Compressed image capture state"""
    
    
    MAGICK_Capture_DISV: BinaryPV
    
    """Compressed image capture state"""
    
    
    MAGICK_Capture_RBV: BinaryPV
    
    """Compressed image capture state (readback)"""
    
    
    MAGICK_FileName: StringPV
    
    """Last saved HDF compressed image name"""
    
    
    MAGICK_FileName_RBV: StringPV
    
    """Last saved compressed image name readback"""
    
    
    MAGICK_FileNumber: ScalarPV
    
    """Not sure"""
    
    
    MAGICK_FileNumber_RBV: StatisticalPV
    
    """Not sure"""
    
    
    MAGICK_FilePath: StringPV
    
    """File path to claraserv3 compressed image (server path not indicated)"""
    
    
    MAGICK_FilePath_RBV: StringPV
    
    """File path to claraserv3 compressed image (server path not indicated)"""
    
    
    MAGICK_FileWriteMode: StatePV
    
    """Save mode for compressed images."""
    
    
    MAGICK_NumCapture: ScalarPV
    
    """Number of compressed images to collect"""
    
    
    MAGICK_NumCapture_RBV: ScalarPV
    
    """Number of compressed images to collect"""
    
    
    MAGICK_WriteFile: BinaryPV
    
    """Write compressed file"""
    
    
    MAGICK_WriteFile_RBV: BinaryPV
    
    """Gets the state of writing procedure for compressed file."""
    
    
    MAGICK_WriteMessage: StringPV
    
    """Not sure"""
    
    
    MAGICK_WriteStatus: BinaryPV
    
    """Gets the writing status for compressed file."""
    
    
    ROI1_ImageData_RBV: WaveformPV
    
    """Camera array data inside ROI"""
    
    
    ROI1_MinX: StatisticalPV
    
    """Horizontal minimum inside ROI"""
    
    
    ROI1_MinX_RBV: StatisticalPV
    
    """Horizontal minimum inside ROI (readback)"""
    
    
    ROI1_MinY: StatisticalPV
    
    """Vertical minimum inside ROI"""
    
    
    ROI1_MinY_RBV: StatisticalPV
    
    """Vertical minimum inside ROI (readback)"""
    
    
    ROI1_SizeX: StatisticalPV
    
    """ROI horizontal size"""
    
    
    ROI1_SizeX_RBV: StatisticalPV
    
    """None"""
    
    
    ROI1_SizeY: StatisticalPV
    
    """ROI vertical size"""
    
    
    ROI1_SizeY_RBV: StatisticalPV
    
    """None"""
    
    
    ROIandMask_SetX: StatisticalPV
    
    """Set ROI horizontal position"""
    
    
    ROIandMask_SetXrad: StatisticalPV
    
    """Set ROI horizontal radius"""
    
    
    ROIandMask_SetY: StatisticalPV
    
    """Set ROI vertical position"""
    
    
    ROIandMask_SetYrad: StatisticalPV
    
    """Set ROI vertical radius"""
    
    
    Reset_Buffer: BinaryPV
    
    """Reset (clear) buffer"""
    
    
    Save: BinaryPV
    
    """Start image save procedure"""
    
    
    Save_Buffer: BinaryPV
    
    """Start image buffer save procedure"""
    
    
    Save_Buffer_Path_Initialise: BinaryPV
    
    """Initialise image buffer save path"""
    
    
    Save_Path_Initialise: BinaryPV
    
    """Initialise image save path"""
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        CameraPVMapModel.is_virtual = is_virtual
        CameraPVMapModel.connect_on_creation = connect_on_creation
        super(
            CameraPVMapModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def ana_avgintensity_rbv(self):
        """Default Getter implementation for ANA_AvgIntensity_RBV"""
        
        return self.ANA_AvgIntensity_RBV.get()
        

    
    
    @property
    def ana_cpu_cropsubmask_rbv(self):
        """Default Getter implementation for ANA_CPU_CropSubMask_RBV"""
        
        return self.ANA_CPU_CropSubMask_RBV.get()
        

    
    
    @property
    def ana_cpu_dot_rbv(self):
        """Default Getter implementation for ANA_CPU_Dot_RBV"""
        
        return self.ANA_CPU_Dot_RBV.get()
        

    
    
    @property
    def ana_cpu_npoint_rbv(self):
        """Default Getter implementation for ANA_CPU_Npoint_RBV"""
        
        return self.ANA_CPU_Npoint_RBV.get()
        

    
    
    @property
    def ana_cpu_rbv(self):
        """Default Getter implementation for ANA_CPU_RBV"""
        
        return self.ANA_CPU_RBV.get()
        

    
    
    @property
    def ana_centerx(self):
        """Default Getter implementation for ANA_CenterX"""
        
        return self.ANA_CenterX.get()
        

    
    
    @property
    def ana_centerx_rbv(self):
        """Default Getter implementation for ANA_CenterX_RBV"""
        
        return self.ANA_CenterX_RBV.get()
        

    
    
    @property
    def ana_centery(self):
        """Default Getter implementation for ANA_CenterY"""
        
        return self.ANA_CenterY.get()
        

    
    
    @property
    def ana_centery_rbv(self):
        """Default Getter implementation for ANA_CenterY_RBV"""
        
        return self.ANA_CenterY_RBV.get()
        

    
    
    @property
    def ana_covxypix_rbv(self):
        """Default Getter implementation for ANA_CovXYPix_RBV"""
        
        return self.ANA_CovXYPix_RBV.get()
        

    
    
    @property
    def ana_covxy_rbv(self):
        """Default Getter implementation for ANA_CovXY_RBV"""
        
        return self.ANA_CovXY_RBV.get()
        

    
    
    @property
    def ana_enablecallbacks(self):
        """Default Getter implementation for ANA_EnableCallbacks"""
        
        return self.ANA_EnableCallbacks.get()
        

    
    @ana_enablecallbacks.setter
    def ana_enablecallbacks(self, value):
        """Default Setter implementation for ANA_EnableCallbacks"""
        
        return self.ANA_EnableCallbacks.put(value)
        
    
    
    @property
    def ana_enablecallbacks_rbv(self):
        """Default Getter implementation for ANA_EnableCallbacks_RBV"""
        
        return self.ANA_EnableCallbacks_RBV.get()
        

    
    
    @property
    def ana_floorlevel(self):
        """Default Getter implementation for ANA_FloorLevel"""
        
        return self.ANA_FloorLevel.get()
        

    
    
    @property
    def ana_floorlevel_rbv(self):
        """Default Getter implementation for ANA_FloorLevel_RBV"""
        
        return self.ANA_FloorLevel_RBV.get()
        

    
    
    @property
    def ana_flooredpercent_rbv(self):
        """Default Getter implementation for ANA_FlooredPercent_RBV"""
        
        return self.ANA_FlooredPercent_RBV.get()
        

    
    
    @property
    def ana_flooredpoints_rbv(self):
        """Default Getter implementation for ANA_FlooredPoints_RBV"""
        
        return self.ANA_FlooredPoints_RBV.get()
        

    
    
    @property
    def ana_intensity_rbv(self):
        """Default Getter implementation for ANA_Intensity_RBV"""
        
        return self.ANA_Intensity_RBV.get()
        

    
    
    @property
    def ana_mmresults_rbv(self):
        """Default Getter implementation for ANA_MMResults_RBV"""
        
        return self.ANA_MMResults_RBV.get()
        

    
    
    @property
    def ana_maskheight_rbv(self):
        """Default Getter implementation for ANA_MaskHeight_RBV"""
        
        return self.ANA_MaskHeight_RBV.get()
        

    
    
    @property
    def ana_maskwidth_rbv(self):
        """Default Getter implementation for ANA_MaskWidth_RBV"""
        
        return self.ANA_MaskWidth_RBV.get()
        

    
    
    @property
    def ana_maskxcenter(self):
        """Default Getter implementation for ANA_MaskXCenter"""
        
        return self.ANA_MaskXCenter.get()
        

    
    
    @property
    def ana_maskxcenter_rbv(self):
        """Default Getter implementation for ANA_MaskXCenter_RBV"""
        
        return self.ANA_MaskXCenter_RBV.get()
        

    
    
    @property
    def ana_maskxrad(self):
        """Default Getter implementation for ANA_MaskXRad"""
        
        return self.ANA_MaskXRad.get()
        

    
    
    @property
    def ana_maskxrad_rbv(self):
        """Default Getter implementation for ANA_MaskXRad_RBV"""
        
        return self.ANA_MaskXRad_RBV.get()
        

    
    
    @property
    def ana_maskycenter(self):
        """Default Getter implementation for ANA_MaskYCenter"""
        
        return self.ANA_MaskYCenter.get()
        

    
    
    @property
    def ana_maskycenter_rbv(self):
        """Default Getter implementation for ANA_MaskYCenter_RBV"""
        
        return self.ANA_MaskYCenter_RBV.get()
        

    
    
    @property
    def ana_maskyrad(self):
        """Default Getter implementation for ANA_MaskYRad"""
        
        return self.ANA_MaskYRad.get()
        

    
    
    @property
    def ana_maskyrad_rbv(self):
        """Default Getter implementation for ANA_MaskYRad_RBV"""
        
        return self.ANA_MaskYRad_RBV.get()
        

    
    
    @property
    def ana_npointstepsize(self):
        """Default Getter implementation for ANA_NPointStepSize"""
        
        return self.ANA_NPointStepSize.get()
        

    
    
    @property
    def ana_npointstepsize_rbv(self):
        """Default Getter implementation for ANA_NPointStepSize_RBV"""
        
        return self.ANA_NPointStepSize_RBV.get()
        

    
    
    @property
    def ana_newbkgrnd(self):
        """Default Getter implementation for ANA_NewBkgrnd"""
        
        return self.ANA_NewBkgrnd.get()
        

    
    
    @property
    def ana_newbkgrnd_rbv(self):
        """Default Getter implementation for ANA_NewBkgrnd_RBV"""
        
        return self.ANA_NewBkgrnd_RBV.get()
        

    
    
    @property
    def ana_overlay_1_cross(self):
        """Default Getter implementation for ANA_OVERLAY_1_CROSS"""
        
        return self.ANA_OVERLAY_1_CROSS.get()
        

    
    
    @property
    def ana_overlay_1_cross_rbv(self):
        """Default Getter implementation for ANA_OVERLAY_1_CROSS_RBV"""
        
        return self.ANA_OVERLAY_1_CROSS_RBV.get()
        

    
    
    @property
    def ana_overlay_2_result(self):
        """Default Getter implementation for ANA_OVERLAY_2_RESULT"""
        
        return self.ANA_OVERLAY_2_RESULT.get()
        

    
    
    @property
    def ana_overlay_2_result_rbv(self):
        """Default Getter implementation for ANA_OVERLAY_2_RESULT_RBV"""
        
        return self.ANA_OVERLAY_2_RESULT_RBV.get()
        

    
    
    @property
    def ana_overlay_3_mask(self):
        """Default Getter implementation for ANA_OVERLAY_3_MASK"""
        
        return self.ANA_OVERLAY_3_MASK.get()
        

    
    
    @property
    def ana_overlay_3_mask_rbv(self):
        """Default Getter implementation for ANA_OVERLAY_3_MASK_RBV"""
        
        return self.ANA_OVERLAY_3_MASK_RBV.get()
        

    
    
    @property
    def ana_pixh_rbv(self):
        """Default Getter implementation for ANA_PixH_RBV"""
        
        return self.ANA_PixH_RBV.get()
        

    
    
    @property
    def ana_pixmm(self):
        """Default Getter implementation for ANA_PixMM"""
        
        return self.ANA_PixMM.get()
        

    
    
    @property
    def ana_pixmm_rbv(self):
        """Default Getter implementation for ANA_PixMM_RBV"""
        
        return self.ANA_PixMM_RBV.get()
        

    
    
    @property
    def ana_pixw_rbv(self):
        """Default Getter implementation for ANA_PixW_RBV"""
        
        return self.ANA_PixW_RBV.get()
        

    
    
    @property
    def ana_pixelresults_rbv(self):
        """Default Getter implementation for ANA_PixelResults_RBV"""
        
        return self.ANA_PixelResults_RBV.get()
        

    
    
    @property
    def ana_sigmaxpix_rbv(self):
        """Default Getter implementation for ANA_SigmaXPix_RBV"""
        
        return self.ANA_SigmaXPix_RBV.get()
        

    
    
    @property
    def ana_sigmax_rbv(self):
        """Default Getter implementation for ANA_SigmaX_RBV"""
        
        return self.ANA_SigmaX_RBV.get()
        

    
    
    @property
    def ana_sigmaypix_rbv(self):
        """Default Getter implementation for ANA_SigmaYPix_RBV"""
        
        return self.ANA_SigmaYPix_RBV.get()
        

    
    
    @property
    def ana_sigmay_rbv(self):
        """Default Getter implementation for ANA_SigmaY_RBV"""
        
        return self.ANA_SigmaY_RBV.get()
        

    
    
    @property
    def ana_usebkgrnd(self):
        """Default Getter implementation for ANA_UseBkgrnd"""
        
        return self.ANA_UseBkgrnd.get()
        

    
    
    @property
    def ana_usebkgrnd_rbv(self):
        """Default Getter implementation for ANA_UseBkgrnd_RBV"""
        
        return self.ANA_UseBkgrnd_RBV.get()
        

    
    
    @property
    def ana_usefloor(self):
        """Default Getter implementation for ANA_UseFloor"""
        
        return self.ANA_UseFloor.get()
        

    
    
    @property
    def ana_usefloor_rbv(self):
        """Default Getter implementation for ANA_UseFloor_RBV"""
        
        return self.ANA_UseFloor_RBV.get()
        

    
    
    @property
    def ana_usenpoint(self):
        """Default Getter implementation for ANA_UseNPoint"""
        
        return self.ANA_UseNPoint.get()
        

    
    
    @property
    def ana_usenpoint_rbv(self):
        """Default Getter implementation for ANA_UseNPoint_RBV"""
        
        return self.ANA_UseNPoint_RBV.get()
        

    
    
    @property
    def ana_xpix_rbv(self):
        """Default Getter implementation for ANA_XPix_RBV"""
        
        return self.ANA_XPix_RBV.get()
        

    
    
    @property
    def ana_x_rbv(self):
        """Default Getter implementation for ANA_X_RBV"""
        
        return self.ANA_X_RBV.get()
        

    
    
    @property
    def ana_ypix_rbv(self):
        """Default Getter implementation for ANA_YPix_RBV"""
        
        return self.ANA_YPix_RBV.get()
        

    
    
    @property
    def ana_y_rbv(self):
        """Default Getter implementation for ANA_Y_RBV"""
        
        return self.ANA_Y_RBV.get()
        

    
    
    @property
    def buffer_status(self):
        """Default Getter implementation for Buffer_Status"""
        
        return self.Buffer_Status.get()
        

    
    
    @property
    def cam1_arraydata(self):
        """Default Getter implementation for CAM1_ArrayData"""
        
        return self.CAM1_ArrayData.get()
        

    
    
    @property
    def cam2_arraydata(self):
        """Default Getter implementation for CAM2_ArrayData"""
        
        return self.CAM2_ArrayData.get()
        

    
    
    @property
    def cam_acquireperiod_rbv(self):
        """Default Getter implementation for CAM_AcquirePeriod_RBV"""
        
        return self.CAM_AcquirePeriod_RBV.get()
        

    
    
    @property
    def cam_acquiretime_rbv(self):
        """Default Getter implementation for CAM_AcquireTime_RBV"""
        
        return self.CAM_AcquireTime_RBV.get()
        

    
    
    @property
    def cam_acquire_rbv(self):
        """Default Getter implementation for CAM_Acquire_RBV"""
        
        return self.CAM_Acquire_RBV.get()
        

    
    
    @property
    def cam_active_count(self):
        """Default Getter implementation for CAM_Active_Count"""
        
        return self.CAM_Active_Count.get()
        

    
    
    @property
    def cam_active_limit(self):
        """Default Getter implementation for CAM_Active_Limit"""
        
        return self.CAM_Active_Limit.get()
        

    
    
    @property
    def cam_arrayrate_rbv(self):
        """Default Getter implementation for CAM_ArrayRate_RBV"""
        
        return self.CAM_ArrayRate_RBV.get()
        

    
    
    @property
    def cam_start_acquire(self):
        """Default Getter implementation for CAM_Start_Acquire"""
        
        return self.CAM_Start_Acquire.get()
        

    
    @cam_start_acquire.setter
    def cam_start_acquire(self, value):
        """Default Setter implementation for CAM_Start_Acquire"""
        
        return self.CAM_Start_Acquire.put(value)
        
    
    
    @property
    def cam_stop_acquire(self):
        """Default Getter implementation for CAM_Stop_Acquire"""
        
        return self.CAM_Stop_Acquire.get()
        

    
    @cam_stop_acquire.setter
    def cam_stop_acquire(self, value):
        """Default Setter implementation for CAM_Stop_Acquire"""
        
        return self.CAM_Stop_Acquire.put(value)
        
    
    
    @property
    def cam_temperature_rbv(self):
        """Default Getter implementation for CAM_Temperature_RBV"""
        
        return self.CAM_Temperature_RBV.get()
        

    
    
    @property
    def hdfb_autosave(self):
        """Default Getter implementation for HDFB_AutoSave"""
        
        return self.HDFB_AutoSave.get()
        

    
    @hdfb_autosave.setter
    def hdfb_autosave(self, value):
        """Default Setter implementation for HDFB_AutoSave"""
        
        return self.HDFB_AutoSave.put(value)
        
    
    
    @property
    def hdfb_buffer_filenumber(self):
        """Default Getter implementation for HDFB_Buffer_FileNumber"""
        
        return self.HDFB_Buffer_FileNumber.get()
        

    
    
    @property
    def hdfb_buffer_filenumber_rbv(self):
        """Default Getter implementation for HDFB_Buffer_FileNumber_RBV"""
        
        return self.HDFB_Buffer_FileNumber_RBV.get()
        

    
    
    @property
    def hdfb_capture(self):
        """Default Getter implementation for HDFB_Capture"""
        
        return self.HDFB_Capture.get()
        

    
    @hdfb_capture.setter
    def hdfb_capture(self, value):
        """Default Setter implementation for HDFB_Capture"""
        
        return self.HDFB_Capture.put(value)
        
    
    
    @property
    def hdfb_capture_disv(self):
        """Default Getter implementation for HDFB_Capture_DISV"""
        
        return self.HDFB_Capture_DISV.get()
        

    
    @hdfb_capture_disv.setter
    def hdfb_capture_disv(self, value):
        """Default Setter implementation for HDFB_Capture_DISV"""
        
        return self.HDFB_Capture_DISV.put(value)
        
    
    
    @property
    def hdfb_capture_rbv(self):
        """Default Getter implementation for HDFB_Capture_RBV"""
        
        return self.HDFB_Capture_RBV.get()
        

    
    
    @property
    def hdfb_filename(self):
        """Default Getter implementation for HDFB_FileName"""
        
        return self.HDFB_FileName.get()
        

    
    
    @property
    def hdfb_filename_rbv(self):
        """Default Getter implementation for HDFB_FileName_RBV"""
        
        return self.HDFB_FileName_RBV.get()
        

    
    
    @property
    def hdfb_filenumber(self):
        """Default Getter implementation for HDFB_FileNumber"""
        
        return self.HDFB_FileNumber.get()
        

    
    
    @property
    def hdfb_filenumber_rbv(self):
        """Default Getter implementation for HDFB_FileNumber_RBV"""
        
        return self.HDFB_FileNumber_RBV.get()
        

    
    
    @property
    def hdfb_filepath(self):
        """Default Getter implementation for HDFB_FilePath"""
        
        return self.HDFB_FilePath.get()
        

    
    
    @property
    def hdfb_filepath_rbv(self):
        """Default Getter implementation for HDFB_FilePath_RBV"""
        
        return self.HDFB_FilePath_RBV.get()
        

    
    
    @property
    def hdfb_filewritemode(self):
        """Default Getter implementation for HDFB_FileWriteMode"""
        
        return self.HDFB_FileWriteMode.get()
        

    
    @hdfb_filewritemode.setter
    def hdfb_filewritemode(self, value):
        """Default Setter implementation for HDFB_FileWriteMode"""
        
        return self.HDFB_FileWriteMode.put(value)
        
    
    
    @property
    def hdfb_numcapture(self):
        """Default Getter implementation for HDFB_NumCapture"""
        
        return self.HDFB_NumCapture.get()
        

    
    @hdfb_numcapture.setter
    def hdfb_numcapture(self, value):
        """Default Setter implementation for HDFB_NumCapture"""
        
        return self.HDFB_NumCapture.put(value)
        
    
    
    @property
    def hdfb_numcapture_rbv(self):
        """Default Getter implementation for HDFB_NumCapture_RBV"""
        
        return self.HDFB_NumCapture_RBV.get()
        

    
    
    @property
    def hdfb_numcaptured_rbv(self):
        """Default Getter implementation for HDFB_NumCaptured_RBV"""
        
        return self.HDFB_NumCaptured_RBV.get()
        

    
    
    @property
    def hdfb_numimagescached_rbv(self):
        """Default Getter implementation for HDFB_NumImagesCached_RBV"""
        
        return self.HDFB_NumImagesCached_RBV.get()
        

    
    
    @property
    def hdfb_postcount(self):
        """Default Getter implementation for HDFB_PostCount"""
        
        return self.HDFB_PostCount.get()
        

    
    @hdfb_postcount.setter
    def hdfb_postcount(self, value):
        """Default Setter implementation for HDFB_PostCount"""
        
        return self.HDFB_PostCount.put(value)
        
    
    
    @property
    def hdfb_precount(self):
        """Default Getter implementation for HDFB_PreCount"""
        
        return self.HDFB_PreCount.get()
        

    
    @hdfb_precount.setter
    def hdfb_precount(self, value):
        """Default Setter implementation for HDFB_PreCount"""
        
        return self.HDFB_PreCount.put(value)
        
    
    
    @property
    def hdfb_writefile(self):
        """Default Getter implementation for HDFB_WriteFile"""
        
        return self.HDFB_WriteFile.get()
        

    
    
    @property
    def hdfb_writefile_rbv(self):
        """Default Getter implementation for HDFB_WriteFile_RBV"""
        
        return self.HDFB_WriteFile_RBV.get()
        

    
    
    @property
    def hdfb_writemessage(self):
        """Default Getter implementation for HDFB_WriteMessage"""
        
        return self.HDFB_WriteMessage.get()
        

    
    
    @property
    def hdfb_writestatus(self):
        """Default Getter implementation for HDFB_WriteStatus"""
        
        return self.HDFB_WriteStatus.get()
        

    
    
    @property
    def hdfb_image_buffer_filename(self):
        """Default Getter implementation for HDFB_image_buffer_fileName"""
        
        return self.HDFB_image_buffer_fileName.get()
        

    
    
    @property
    def hdfb_image_buffer_filename_rbv(self):
        """Default Getter implementation for HDFB_image_buffer_fileName_RBV"""
        
        return self.HDFB_image_buffer_fileName_RBV.get()
        

    
    
    @property
    def hdfb_image_buffer_filepath(self):
        """Default Getter implementation for HDFB_image_buffer_filePath"""
        
        return self.HDFB_image_buffer_filePath.get()
        

    
    
    @property
    def hdfb_image_buffer_filepath_rbv(self):
        """Default Getter implementation for HDFB_image_buffer_filePath_RBV"""
        
        return self.HDFB_image_buffer_filePath_RBV.get()
        

    
    
    @property
    def hdfb_image_buffer_trigger(self):
        """Default Getter implementation for HDFB_image_buffer_trigger"""
        
        return self.HDFB_image_buffer_trigger.get()
        

    
    
    @property
    def hdfm_autosave(self):
        """Default Getter implementation for HDFM_AutoSave"""
        
        return self.HDFM_AutoSave.get()
        

    
    @hdfm_autosave.setter
    def hdfm_autosave(self, value):
        """Default Setter implementation for HDFM_AutoSave"""
        
        return self.HDFM_AutoSave.put(value)
        
    
    
    @property
    def hdfm_capture(self):
        """Default Getter implementation for HDFM_Capture"""
        
        return self.HDFM_Capture.get()
        

    
    @hdfm_capture.setter
    def hdfm_capture(self, value):
        """Default Setter implementation for HDFM_Capture"""
        
        return self.HDFM_Capture.put(value)
        
    
    
    @property
    def hdfm_capture_disv(self):
        """Default Getter implementation for HDFM_Capture_DISV"""
        
        return self.HDFM_Capture_DISV.get()
        

    
    @hdfm_capture_disv.setter
    def hdfm_capture_disv(self, value):
        """Default Setter implementation for HDFM_Capture_DISV"""
        
        return self.HDFM_Capture_DISV.put(value)
        
    
    
    @property
    def hdfm_capture_rbv(self):
        """Default Getter implementation for HDFM_Capture_RBV"""
        
        return self.HDFM_Capture_RBV.get()
        

    
    
    @property
    def hdfm_filename(self):
        """Default Getter implementation for HDFM_FileName"""
        
        return self.HDFM_FileName.get()
        

    
    
    @property
    def hdfm_filename_rbv(self):
        """Default Getter implementation for HDFM_FileName_RBV"""
        
        return self.HDFM_FileName_RBV.get()
        

    
    
    @property
    def hdfm_filenumber(self):
        """Default Getter implementation for HDFM_FileNumber"""
        
        return self.HDFM_FileNumber.get()
        

    
    
    @property
    def hdfm_filenumber_rbv(self):
        """Default Getter implementation for HDFM_FileNumber_RBV"""
        
        return self.HDFM_FileNumber_RBV.get()
        

    
    
    @property
    def hdfm_filepath(self):
        """Default Getter implementation for HDFM_FilePath"""
        
        return self.HDFM_FilePath.get()
        

    
    
    @property
    def hdfm_filepath_rbv(self):
        """Default Getter implementation for HDFM_FilePath_RBV"""
        
        return self.HDFM_FilePath_RBV.get()
        

    
    
    @property
    def hdfm_filewritemode(self):
        """Default Getter implementation for HDFM_FileWriteMode"""
        
        return self.HDFM_FileWriteMode.get()
        

    
    @hdfm_filewritemode.setter
    def hdfm_filewritemode(self, value):
        """Default Setter implementation for HDFM_FileWriteMode"""
        
        return self.HDFM_FileWriteMode.put(value)
        
    
    
    @property
    def hdfm_numcapture(self):
        """Default Getter implementation for HDFM_NumCapture"""
        
        return self.HDFM_NumCapture.get()
        

    
    @hdfm_numcapture.setter
    def hdfm_numcapture(self, value):
        """Default Setter implementation for HDFM_NumCapture"""
        
        return self.HDFM_NumCapture.put(value)
        
    
    
    @property
    def hdfm_numcapture_rbv(self):
        """Default Getter implementation for HDFM_NumCapture_RBV"""
        
        return self.HDFM_NumCapture_RBV.get()
        

    
    
    @property
    def hdfm_writefile(self):
        """Default Getter implementation for HDFM_WriteFile"""
        
        return self.HDFM_WriteFile.get()
        

    
    
    @property
    def hdfm_writefile_rbv(self):
        """Default Getter implementation for HDFM_WriteFile_RBV"""
        
        return self.HDFM_WriteFile_RBV.get()
        

    
    
    @property
    def hdfm_writemessage(self):
        """Default Getter implementation for HDFM_WriteMessage"""
        
        return self.HDFM_WriteMessage.get()
        

    
    
    @property
    def hdfm_writestatus(self):
        """Default Getter implementation for HDFM_WriteStatus"""
        
        return self.HDFM_WriteStatus.get()
        

    
    
    @property
    def hdf_autosave(self):
        """Default Getter implementation for HDF_AutoSave"""
        
        return self.HDF_AutoSave.get()
        

    
    @hdf_autosave.setter
    def hdf_autosave(self, value):
        """Default Setter implementation for HDF_AutoSave"""
        
        return self.HDF_AutoSave.put(value)
        
    
    
    @property
    def hdf_capture(self):
        """Default Getter implementation for HDF_Capture"""
        
        return self.HDF_Capture.get()
        

    
    @hdf_capture.setter
    def hdf_capture(self, value):
        """Default Setter implementation for HDF_Capture"""
        
        return self.HDF_Capture.put(value)
        
    
    
    @property
    def hdf_capture_disv(self):
        """Default Getter implementation for HDF_Capture_DISV"""
        
        return self.HDF_Capture_DISV.get()
        

    
    @hdf_capture_disv.setter
    def hdf_capture_disv(self, value):
        """Default Setter implementation for HDF_Capture_DISV"""
        
        return self.HDF_Capture_DISV.put(value)
        
    
    
    @property
    def hdf_capture_rbv(self):
        """Default Getter implementation for HDF_Capture_RBV"""
        
        return self.HDF_Capture_RBV.get()
        

    
    
    @property
    def hdf_filename(self):
        """Default Getter implementation for HDF_FileName"""
        
        return self.HDF_FileName.get()
        

    
    
    @property
    def hdf_filename_rbv(self):
        """Default Getter implementation for HDF_FileName_RBV"""
        
        return self.HDF_FileName_RBV.get()
        

    
    
    @property
    def hdf_filenumber(self):
        """Default Getter implementation for HDF_FileNumber"""
        
        return self.HDF_FileNumber.get()
        

    
    
    @property
    def hdf_filenumber_rbv(self):
        """Default Getter implementation for HDF_FileNumber_RBV"""
        
        return self.HDF_FileNumber_RBV.get()
        

    
    
    @property
    def hdf_filepath(self):
        """Default Getter implementation for HDF_FilePath"""
        
        return self.HDF_FilePath.get()
        

    
    
    @property
    def hdf_filepath_rbv(self):
        """Default Getter implementation for HDF_FilePath_RBV"""
        
        return self.HDF_FilePath_RBV.get()
        

    
    
    @property
    def hdf_filewritemode(self):
        """Default Getter implementation for HDF_FileWriteMode"""
        
        return self.HDF_FileWriteMode.get()
        

    
    @hdf_filewritemode.setter
    def hdf_filewritemode(self, value):
        """Default Setter implementation for HDF_FileWriteMode"""
        
        return self.HDF_FileWriteMode.put(value)
        
    
    
    @property
    def hdf_numcapture(self):
        """Default Getter implementation for HDF_NumCapture"""
        
        return self.HDF_NumCapture.get()
        

    
    @hdf_numcapture.setter
    def hdf_numcapture(self, value):
        """Default Setter implementation for HDF_NumCapture"""
        
        return self.HDF_NumCapture.put(value)
        
    
    
    @property
    def hdf_numcapture_rbv(self):
        """Default Getter implementation for HDF_NumCapture_RBV"""
        
        return self.HDF_NumCapture_RBV.get()
        

    
    
    @property
    def hdf_writefile(self):
        """Default Getter implementation for HDF_WriteFile"""
        
        return self.HDF_WriteFile.get()
        

    
    
    @property
    def hdf_writefile_rbv(self):
        """Default Getter implementation for HDF_WriteFile_RBV"""
        
        return self.HDF_WriteFile_RBV.get()
        

    
    
    @property
    def hdf_writemessage(self):
        """Default Getter implementation for HDF_WriteMessage"""
        
        return self.HDF_WriteMessage.get()
        

    
    
    @property
    def hdf_writestatus(self):
        """Default Getter implementation for HDF_WriteStatus"""
        
        return self.HDF_WriteStatus.get()
        

    
    
    @property
    def init_buffer(self):
        """Default Getter implementation for Init_Buffer"""
        
        return self.Init_Buffer.get()
        

    
    @init_buffer.setter
    def init_buffer(self, value):
        """Default Setter implementation for Init_Buffer"""
        
        return self.Init_Buffer.put(value)
        
    
    
    @property
    def led_off(self):
        """Default Getter implementation for LED_Off"""
        
        return self.LED_Off.get()
        

    
    @led_off.setter
    def led_off(self, value):
        """Default Setter implementation for LED_Off"""
        
        return self.LED_Off.put(value)
        
    
    
    @property
    def led_on(self):
        """Default Getter implementation for LED_On"""
        
        return self.LED_On.get()
        

    
    @led_on.setter
    def led_on(self, value):
        """Default Setter implementation for LED_On"""
        
        return self.LED_On.put(value)
        
    
    
    @property
    def led_sta(self):
        """Default Getter implementation for LED_Sta"""
        
        return self.LED_Sta.get()
        

    
    
    @property
    def magick_autosave(self):
        """Default Getter implementation for MAGICK_AutoSave"""
        
        return self.MAGICK_AutoSave.get()
        

    
    @magick_autosave.setter
    def magick_autosave(self, value):
        """Default Setter implementation for MAGICK_AutoSave"""
        
        return self.MAGICK_AutoSave.put(value)
        
    
    
    @property
    def magick_capture(self):
        """Default Getter implementation for MAGICK_Capture"""
        
        return self.MAGICK_Capture.get()
        

    
    @magick_capture.setter
    def magick_capture(self, value):
        """Default Setter implementation for MAGICK_Capture"""
        
        return self.MAGICK_Capture.put(value)
        
    
    
    @property
    def magick_capture_disv(self):
        """Default Getter implementation for MAGICK_Capture_DISV"""
        
        return self.MAGICK_Capture_DISV.get()
        

    
    @magick_capture_disv.setter
    def magick_capture_disv(self, value):
        """Default Setter implementation for MAGICK_Capture_DISV"""
        
        return self.MAGICK_Capture_DISV.put(value)
        
    
    
    @property
    def magick_capture_rbv(self):
        """Default Getter implementation for MAGICK_Capture_RBV"""
        
        return self.MAGICK_Capture_RBV.get()
        

    
    
    @property
    def magick_filename(self):
        """Default Getter implementation for MAGICK_FileName"""
        
        return self.MAGICK_FileName.get()
        

    
    
    @property
    def magick_filename_rbv(self):
        """Default Getter implementation for MAGICK_FileName_RBV"""
        
        return self.MAGICK_FileName_RBV.get()
        

    
    
    @property
    def magick_filenumber(self):
        """Default Getter implementation for MAGICK_FileNumber"""
        
        return self.MAGICK_FileNumber.get()
        

    
    
    @property
    def magick_filenumber_rbv(self):
        """Default Getter implementation for MAGICK_FileNumber_RBV"""
        
        return self.MAGICK_FileNumber_RBV.get()
        

    
    
    @property
    def magick_filepath(self):
        """Default Getter implementation for MAGICK_FilePath"""
        
        return self.MAGICK_FilePath.get()
        

    
    
    @property
    def magick_filepath_rbv(self):
        """Default Getter implementation for MAGICK_FilePath_RBV"""
        
        return self.MAGICK_FilePath_RBV.get()
        

    
    
    @property
    def magick_filewritemode(self):
        """Default Getter implementation for MAGICK_FileWriteMode"""
        
        return self.MAGICK_FileWriteMode.get()
        

    
    @magick_filewritemode.setter
    def magick_filewritemode(self, value):
        """Default Setter implementation for MAGICK_FileWriteMode"""
        
        return self.MAGICK_FileWriteMode.put(value)
        
    
    
    @property
    def magick_numcapture(self):
        """Default Getter implementation for MAGICK_NumCapture"""
        
        return self.MAGICK_NumCapture.get()
        

    
    @magick_numcapture.setter
    def magick_numcapture(self, value):
        """Default Setter implementation for MAGICK_NumCapture"""
        
        return self.MAGICK_NumCapture.put(value)
        
    
    
    @property
    def magick_numcapture_rbv(self):
        """Default Getter implementation for MAGICK_NumCapture_RBV"""
        
        return self.MAGICK_NumCapture_RBV.get()
        

    
    
    @property
    def magick_writefile(self):
        """Default Getter implementation for MAGICK_WriteFile"""
        
        return self.MAGICK_WriteFile.get()
        

    
    
    @property
    def magick_writefile_rbv(self):
        """Default Getter implementation for MAGICK_WriteFile_RBV"""
        
        return self.MAGICK_WriteFile_RBV.get()
        

    
    
    @property
    def magick_writemessage(self):
        """Default Getter implementation for MAGICK_WriteMessage"""
        
        return self.MAGICK_WriteMessage.get()
        

    
    
    @property
    def magick_writestatus(self):
        """Default Getter implementation for MAGICK_WriteStatus"""
        
        return self.MAGICK_WriteStatus.get()
        

    
    
    @property
    def roi1_imagedata_rbv(self):
        """Default Getter implementation for ROI1_ImageData_RBV"""
        
        return self.ROI1_ImageData_RBV.get()
        

    
    
    @property
    def roi1_minx(self):
        """Default Getter implementation for ROI1_MinX"""
        
        return self.ROI1_MinX.get()
        

    
    
    @property
    def roi1_minx_rbv(self):
        """Default Getter implementation for ROI1_MinX_RBV"""
        
        return self.ROI1_MinX_RBV.get()
        

    
    
    @property
    def roi1_miny(self):
        """Default Getter implementation for ROI1_MinY"""
        
        return self.ROI1_MinY.get()
        

    
    
    @property
    def roi1_miny_rbv(self):
        """Default Getter implementation for ROI1_MinY_RBV"""
        
        return self.ROI1_MinY_RBV.get()
        

    
    
    @property
    def roi1_sizex(self):
        """Default Getter implementation for ROI1_SizeX"""
        
        return self.ROI1_SizeX.get()
        

    
    
    @property
    def roi1_sizex_rbv(self):
        """Default Getter implementation for ROI1_SizeX_RBV"""
        
        return self.ROI1_SizeX_RBV.get()
        

    
    
    @property
    def roi1_sizey(self):
        """Default Getter implementation for ROI1_SizeY"""
        
        return self.ROI1_SizeY.get()
        

    
    
    @property
    def roi1_sizey_rbv(self):
        """Default Getter implementation for ROI1_SizeY_RBV"""
        
        return self.ROI1_SizeY_RBV.get()
        

    
    
    @property
    def roiandmask_setx(self):
        """Default Getter implementation for ROIandMask_SetX"""
        
        return self.ROIandMask_SetX.get()
        

    
    
    @property
    def roiandmask_setxrad(self):
        """Default Getter implementation for ROIandMask_SetXrad"""
        
        return self.ROIandMask_SetXrad.get()
        

    
    
    @property
    def roiandmask_sety(self):
        """Default Getter implementation for ROIandMask_SetY"""
        
        return self.ROIandMask_SetY.get()
        

    
    
    @property
    def roiandmask_setyrad(self):
        """Default Getter implementation for ROIandMask_SetYrad"""
        
        return self.ROIandMask_SetYrad.get()
        

    
    
    @property
    def reset_buffer(self):
        """Default Getter implementation for Reset_Buffer"""
        
        return self.Reset_Buffer.get()
        

    
    @reset_buffer.setter
    def reset_buffer(self, value):
        """Default Setter implementation for Reset_Buffer"""
        
        return self.Reset_Buffer.put(value)
        
    
    
    @property
    def save(self):
        """Default Getter implementation for Save"""
        
        return self.Save.get()
        

    
    @save.setter
    def save(self, value):
        """Default Setter implementation for Save"""
        
        return self.Save.put(value)
        
    
    
    @property
    def save_buffer(self):
        """Default Getter implementation for Save_Buffer"""
        
        return self.Save_Buffer.get()
        

    
    @save_buffer.setter
    def save_buffer(self, value):
        """Default Setter implementation for Save_Buffer"""
        
        return self.Save_Buffer.put(value)
        
    
    
    @property
    def save_buffer_path_initialise(self):
        """Default Getter implementation for Save_Buffer_Path_Initialise"""
        
        return self.Save_Buffer_Path_Initialise.get()
        

    
    @save_buffer_path_initialise.setter
    def save_buffer_path_initialise(self, value):
        """Default Setter implementation for Save_Buffer_Path_Initialise"""
        
        return self.Save_Buffer_Path_Initialise.put(value)
        
    
    
    @property
    def save_path_initialise(self):
        """Default Getter implementation for Save_Path_Initialise"""
        
        return self.Save_Path_Initialise.get()
        

    
    @save_path_initialise.setter
    def save_path_initialise(self, value):
        """Default Setter implementation for Save_Path_Initialise"""
        
        return self.Save_Path_Initialise.put(value)
        
    
    



class CameraControlsInformationModel(ControlsInformation):
    """
    Class for controlling a camera via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[CameraPVMapModel]

    

    """Dictionary of PVs read in from a config file (see :class:`~CATAP.common.machine.hardware.PVMap`)"""
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        extra="allow",
    )

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        CameraControlsInformationModel.is_virtual = is_virtual
        CameraControlsInformationModel.connect_on_creation = connect_on_creation
        super(
            CameraControlsInformationModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> CameraPVMapModel:
        return CameraPVMapModel(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def ana_avgintensity_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_AvgIntensity_RBV`."""    
        return self.pv_record_map.ana_avgintensity_rbv
    
    
    @property
    def ana_cpu_cropsubmask_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_CPU_CropSubMask_RBV`."""    
        return self.pv_record_map.ana_cpu_cropsubmask_rbv
    
    
    @property
    def ana_cpu_dot_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_CPU_Dot_RBV`."""    
        return self.pv_record_map.ana_cpu_dot_rbv
    
    
    @property
    def ana_cpu_npoint_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_CPU_Npoint_RBV`."""    
        return self.pv_record_map.ana_cpu_npoint_rbv
    
    
    @property
    def ana_cpu_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_CPU_RBV`."""    
        return self.pv_record_map.ana_cpu_rbv
    
    
    @property
    def ana_centerx(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_CenterX`."""    
        return self.pv_record_map.ana_centerx
    
    
    @property
    def ana_centerx_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_CenterX_RBV`."""    
        return self.pv_record_map.ana_centerx_rbv
    
    
    @property
    def ana_centery(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_CenterY`."""    
        return self.pv_record_map.ana_centery
    
    
    @property
    def ana_centery_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_CenterY_RBV`."""    
        return self.pv_record_map.ana_centery_rbv
    
    
    @property
    def ana_covxypix_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_CovXYPix_RBV`."""    
        return self.pv_record_map.ana_covxypix_rbv
    
    
    @property
    def ana_covxy_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_CovXY_RBV`."""    
        return self.pv_record_map.ana_covxy_rbv
    
    
    @property
    def ana_enablecallbacks(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_EnableCallbacks`."""    
        return self.pv_record_map.ana_enablecallbacks
    
    @ana_enablecallbacks.setter
    def ana_enablecallbacks(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.ANA_EnableCallbacks`.""" 
        self.pv_record_map.ana_enablecallbacks = value
    
    
    @property
    def ana_enablecallbacks_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_EnableCallbacks_RBV`."""    
        return self.pv_record_map.ana_enablecallbacks_rbv
    
    
    @property
    def ana_floorlevel(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_FloorLevel`."""    
        return self.pv_record_map.ana_floorlevel
    
    
    @property
    def ana_floorlevel_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_FloorLevel_RBV`."""    
        return self.pv_record_map.ana_floorlevel_rbv
    
    
    @property
    def ana_flooredpercent_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_FlooredPercent_RBV`."""    
        return self.pv_record_map.ana_flooredpercent_rbv
    
    
    @property
    def ana_flooredpoints_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_FlooredPoints_RBV`."""    
        return self.pv_record_map.ana_flooredpoints_rbv
    
    
    @property
    def ana_intensity_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_Intensity_RBV`."""    
        return self.pv_record_map.ana_intensity_rbv
    
    
    @property
    def ana_mmresults_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_MMResults_RBV`."""    
        return self.pv_record_map.ana_mmresults_rbv
    
    
    @property
    def ana_maskheight_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_MaskHeight_RBV`."""    
        return self.pv_record_map.ana_maskheight_rbv
    
    
    @property
    def ana_maskwidth_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_MaskWidth_RBV`."""    
        return self.pv_record_map.ana_maskwidth_rbv
    
    
    @property
    def ana_maskxcenter(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_MaskXCenter`."""    
        return self.pv_record_map.ana_maskxcenter
    
    
    @property
    def ana_maskxcenter_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_MaskXCenter_RBV`."""    
        return self.pv_record_map.ana_maskxcenter_rbv
    
    
    @property
    def ana_maskxrad(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_MaskXRad`."""    
        return self.pv_record_map.ana_maskxrad
    
    
    @property
    def ana_maskxrad_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_MaskXRad_RBV`."""    
        return self.pv_record_map.ana_maskxrad_rbv
    
    
    @property
    def ana_maskycenter(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_MaskYCenter`."""    
        return self.pv_record_map.ana_maskycenter
    
    
    @property
    def ana_maskycenter_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_MaskYCenter_RBV`."""    
        return self.pv_record_map.ana_maskycenter_rbv
    
    
    @property
    def ana_maskyrad(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_MaskYRad`."""    
        return self.pv_record_map.ana_maskyrad
    
    
    @property
    def ana_maskyrad_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_MaskYRad_RBV`."""    
        return self.pv_record_map.ana_maskyrad_rbv
    
    
    @property
    def ana_npointstepsize(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_NPointStepSize`."""    
        return self.pv_record_map.ana_npointstepsize
    
    
    @property
    def ana_npointstepsize_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_NPointStepSize_RBV`."""    
        return self.pv_record_map.ana_npointstepsize_rbv
    
    
    @property
    def ana_newbkgrnd(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_NewBkgrnd`."""    
        return self.pv_record_map.ana_newbkgrnd
    
    
    @property
    def ana_newbkgrnd_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_NewBkgrnd_RBV`."""    
        return self.pv_record_map.ana_newbkgrnd_rbv
    
    
    @property
    def ana_overlay_1_cross(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_OVERLAY_1_CROSS`."""    
        return self.pv_record_map.ana_overlay_1_cross
    
    
    @property
    def ana_overlay_1_cross_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_OVERLAY_1_CROSS_RBV`."""    
        return self.pv_record_map.ana_overlay_1_cross_rbv
    
    
    @property
    def ana_overlay_2_result(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_OVERLAY_2_RESULT`."""    
        return self.pv_record_map.ana_overlay_2_result
    
    
    @property
    def ana_overlay_2_result_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_OVERLAY_2_RESULT_RBV`."""    
        return self.pv_record_map.ana_overlay_2_result_rbv
    
    
    @property
    def ana_overlay_3_mask(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_OVERLAY_3_MASK`."""    
        return self.pv_record_map.ana_overlay_3_mask
    
    
    @property
    def ana_overlay_3_mask_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_OVERLAY_3_MASK_RBV`."""    
        return self.pv_record_map.ana_overlay_3_mask_rbv
    
    
    @property
    def ana_pixh_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_PixH_RBV`."""    
        return self.pv_record_map.ana_pixh_rbv
    
    
    @property
    def ana_pixmm(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_PixMM`."""    
        return self.pv_record_map.ana_pixmm
    
    
    @property
    def ana_pixmm_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_PixMM_RBV`."""    
        return self.pv_record_map.ana_pixmm_rbv
    
    
    @property
    def ana_pixw_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_PixW_RBV`."""    
        return self.pv_record_map.ana_pixw_rbv
    
    
    @property
    def ana_pixelresults_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_PixelResults_RBV`."""    
        return self.pv_record_map.ana_pixelresults_rbv
    
    
    @property
    def ana_sigmaxpix_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_SigmaXPix_RBV`."""    
        return self.pv_record_map.ana_sigmaxpix_rbv
    
    
    @property
    def ana_sigmax_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_SigmaX_RBV`."""    
        return self.pv_record_map.ana_sigmax_rbv
    
    
    @property
    def ana_sigmaypix_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_SigmaYPix_RBV`."""    
        return self.pv_record_map.ana_sigmaypix_rbv
    
    
    @property
    def ana_sigmay_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_SigmaY_RBV`."""    
        return self.pv_record_map.ana_sigmay_rbv
    
    
    @property
    def ana_usebkgrnd(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_UseBkgrnd`."""    
        return self.pv_record_map.ana_usebkgrnd
    
    
    @property
    def ana_usebkgrnd_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_UseBkgrnd_RBV`."""    
        return self.pv_record_map.ana_usebkgrnd_rbv
    
    
    @property
    def ana_usefloor(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_UseFloor`."""    
        return self.pv_record_map.ana_usefloor
    
    
    @property
    def ana_usefloor_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_UseFloor_RBV`."""    
        return self.pv_record_map.ana_usefloor_rbv
    
    
    @property
    def ana_usenpoint(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_UseNPoint`."""    
        return self.pv_record_map.ana_usenpoint
    
    
    @property
    def ana_usenpoint_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_UseNPoint_RBV`."""    
        return self.pv_record_map.ana_usenpoint_rbv
    
    
    @property
    def ana_xpix_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_XPix_RBV`."""    
        return self.pv_record_map.ana_xpix_rbv
    
    
    @property
    def ana_x_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_X_RBV`."""    
        return self.pv_record_map.ana_x_rbv
    
    
    @property
    def ana_ypix_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_YPix_RBV`."""    
        return self.pv_record_map.ana_ypix_rbv
    
    
    @property
    def ana_y_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ANA_Y_RBV`."""    
        return self.pv_record_map.ana_y_rbv
    
    
    @property
    def buffer_status(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.Buffer_Status`."""    
        return self.pv_record_map.buffer_status
    
    
    @property
    def cam1_arraydata(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.CAM1_ArrayData`."""    
        return self.pv_record_map.cam1_arraydata
    
    
    @property
    def cam2_arraydata(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.CAM2_ArrayData`."""    
        return self.pv_record_map.cam2_arraydata
    
    
    @property
    def cam_acquireperiod_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.CAM_AcquirePeriod_RBV`."""    
        return self.pv_record_map.cam_acquireperiod_rbv
    
    
    @property
    def cam_acquiretime_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.CAM_AcquireTime_RBV`."""    
        return self.pv_record_map.cam_acquiretime_rbv
    
    
    @property
    def cam_acquire_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.CAM_Acquire_RBV`."""    
        return self.pv_record_map.cam_acquire_rbv
    
    
    @property
    def cam_active_count(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.CAM_Active_Count`."""    
        return self.pv_record_map.cam_active_count
    
    
    @property
    def cam_active_limit(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.CAM_Active_Limit`."""    
        return self.pv_record_map.cam_active_limit
    
    
    @property
    def cam_arrayrate_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.CAM_ArrayRate_RBV`."""    
        return self.pv_record_map.cam_arrayrate_rbv
    
    
    @property
    def cam_start_acquire(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.CAM_Start_Acquire`."""    
        return self.pv_record_map.cam_start_acquire
    
    @cam_start_acquire.setter
    def cam_start_acquire(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.CAM_Start_Acquire`.""" 
        self.pv_record_map.cam_start_acquire = value
    
    
    @property
    def cam_stop_acquire(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.CAM_Stop_Acquire`."""    
        return self.pv_record_map.cam_stop_acquire
    
    @cam_stop_acquire.setter
    def cam_stop_acquire(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.CAM_Stop_Acquire`.""" 
        self.pv_record_map.cam_stop_acquire = value
    
    
    @property
    def cam_temperature_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.CAM_Temperature_RBV`."""    
        return self.pv_record_map.cam_temperature_rbv
    
    
    @property
    def hdfb_autosave(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_AutoSave`."""    
        return self.pv_record_map.hdfb_autosave
    
    @hdfb_autosave.setter
    def hdfb_autosave(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.HDFB_AutoSave`.""" 
        self.pv_record_map.hdfb_autosave = value
    
    
    @property
    def hdfb_buffer_filenumber(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_Buffer_FileNumber`."""    
        return self.pv_record_map.hdfb_buffer_filenumber
    
    
    @property
    def hdfb_buffer_filenumber_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_Buffer_FileNumber_RBV`."""    
        return self.pv_record_map.hdfb_buffer_filenumber_rbv
    
    
    @property
    def hdfb_capture(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_Capture`."""    
        return self.pv_record_map.hdfb_capture
    
    @hdfb_capture.setter
    def hdfb_capture(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.HDFB_Capture`.""" 
        self.pv_record_map.hdfb_capture = value
    
    
    @property
    def hdfb_capture_disv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_Capture_DISV`."""    
        return self.pv_record_map.hdfb_capture_disv
    
    @hdfb_capture_disv.setter
    def hdfb_capture_disv(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.HDFB_Capture_DISV`.""" 
        self.pv_record_map.hdfb_capture_disv = value
    
    
    @property
    def hdfb_capture_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_Capture_RBV`."""    
        return self.pv_record_map.hdfb_capture_rbv
    
    
    @property
    def hdfb_filename(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_FileName`."""    
        return self.pv_record_map.hdfb_filename
    
    
    @property
    def hdfb_filename_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_FileName_RBV`."""    
        return self.pv_record_map.hdfb_filename_rbv
    
    
    @property
    def hdfb_filenumber(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_FileNumber`."""    
        return self.pv_record_map.hdfb_filenumber
    
    
    @property
    def hdfb_filenumber_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_FileNumber_RBV`."""    
        return self.pv_record_map.hdfb_filenumber_rbv
    
    
    @property
    def hdfb_filepath(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_FilePath`."""    
        return self.pv_record_map.hdfb_filepath
    
    
    @property
    def hdfb_filepath_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_FilePath_RBV`."""    
        return self.pv_record_map.hdfb_filepath_rbv
    
    
    @property
    def hdfb_filewritemode(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_FileWriteMode`."""    
        return self.pv_record_map.hdfb_filewritemode
    
    @hdfb_filewritemode.setter
    def hdfb_filewritemode(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.HDFB_FileWriteMode`.""" 
        self.pv_record_map.hdfb_filewritemode = value
    
    
    @property
    def hdfb_numcapture(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_NumCapture`."""    
        return self.pv_record_map.hdfb_numcapture
    
    @hdfb_numcapture.setter
    def hdfb_numcapture(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.HDFB_NumCapture`.""" 
        self.pv_record_map.hdfb_numcapture = value
    
    
    @property
    def hdfb_numcapture_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_NumCapture_RBV`."""    
        return self.pv_record_map.hdfb_numcapture_rbv
    
    
    @property
    def hdfb_numcaptured_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_NumCaptured_RBV`."""    
        return self.pv_record_map.hdfb_numcaptured_rbv
    
    
    @property
    def hdfb_numimagescached_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_NumImagesCached_RBV`."""    
        return self.pv_record_map.hdfb_numimagescached_rbv
    
    
    @property
    def hdfb_postcount(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_PostCount`."""    
        return self.pv_record_map.hdfb_postcount
    
    @hdfb_postcount.setter
    def hdfb_postcount(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.HDFB_PostCount`.""" 
        self.pv_record_map.hdfb_postcount = value
    
    
    @property
    def hdfb_precount(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_PreCount`."""    
        return self.pv_record_map.hdfb_precount
    
    @hdfb_precount.setter
    def hdfb_precount(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.HDFB_PreCount`.""" 
        self.pv_record_map.hdfb_precount = value
    
    
    @property
    def hdfb_writefile(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_WriteFile`."""    
        return self.pv_record_map.hdfb_writefile
    
    
    @property
    def hdfb_writefile_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_WriteFile_RBV`."""    
        return self.pv_record_map.hdfb_writefile_rbv
    
    
    @property
    def hdfb_writemessage(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_WriteMessage`."""    
        return self.pv_record_map.hdfb_writemessage
    
    
    @property
    def hdfb_writestatus(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_WriteStatus`."""    
        return self.pv_record_map.hdfb_writestatus
    
    
    @property
    def hdfb_image_buffer_filename(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_image_buffer_fileName`."""    
        return self.pv_record_map.hdfb_image_buffer_filename
    
    
    @property
    def hdfb_image_buffer_filename_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_image_buffer_fileName_RBV`."""    
        return self.pv_record_map.hdfb_image_buffer_filename_rbv
    
    
    @property
    def hdfb_image_buffer_filepath(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_image_buffer_filePath`."""    
        return self.pv_record_map.hdfb_image_buffer_filepath
    
    
    @property
    def hdfb_image_buffer_filepath_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_image_buffer_filePath_RBV`."""    
        return self.pv_record_map.hdfb_image_buffer_filepath_rbv
    
    
    @property
    def hdfb_image_buffer_trigger(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFB_image_buffer_trigger`."""    
        return self.pv_record_map.hdfb_image_buffer_trigger
    
    
    @property
    def hdfm_autosave(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFM_AutoSave`."""    
        return self.pv_record_map.hdfm_autosave
    
    @hdfm_autosave.setter
    def hdfm_autosave(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.HDFM_AutoSave`.""" 
        self.pv_record_map.hdfm_autosave = value
    
    
    @property
    def hdfm_capture(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFM_Capture`."""    
        return self.pv_record_map.hdfm_capture
    
    @hdfm_capture.setter
    def hdfm_capture(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.HDFM_Capture`.""" 
        self.pv_record_map.hdfm_capture = value
    
    
    @property
    def hdfm_capture_disv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFM_Capture_DISV`."""    
        return self.pv_record_map.hdfm_capture_disv
    
    @hdfm_capture_disv.setter
    def hdfm_capture_disv(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.HDFM_Capture_DISV`.""" 
        self.pv_record_map.hdfm_capture_disv = value
    
    
    @property
    def hdfm_capture_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFM_Capture_RBV`."""    
        return self.pv_record_map.hdfm_capture_rbv
    
    
    @property
    def hdfm_filename(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFM_FileName`."""    
        return self.pv_record_map.hdfm_filename
    
    
    @property
    def hdfm_filename_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFM_FileName_RBV`."""    
        return self.pv_record_map.hdfm_filename_rbv
    
    
    @property
    def hdfm_filenumber(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFM_FileNumber`."""    
        return self.pv_record_map.hdfm_filenumber
    
    
    @property
    def hdfm_filenumber_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFM_FileNumber_RBV`."""    
        return self.pv_record_map.hdfm_filenumber_rbv
    
    
    @property
    def hdfm_filepath(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFM_FilePath`."""    
        return self.pv_record_map.hdfm_filepath
    
    
    @property
    def hdfm_filepath_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFM_FilePath_RBV`."""    
        return self.pv_record_map.hdfm_filepath_rbv
    
    
    @property
    def hdfm_filewritemode(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFM_FileWriteMode`."""    
        return self.pv_record_map.hdfm_filewritemode
    
    @hdfm_filewritemode.setter
    def hdfm_filewritemode(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.HDFM_FileWriteMode`.""" 
        self.pv_record_map.hdfm_filewritemode = value
    
    
    @property
    def hdfm_numcapture(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFM_NumCapture`."""    
        return self.pv_record_map.hdfm_numcapture
    
    @hdfm_numcapture.setter
    def hdfm_numcapture(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.HDFM_NumCapture`.""" 
        self.pv_record_map.hdfm_numcapture = value
    
    
    @property
    def hdfm_numcapture_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFM_NumCapture_RBV`."""    
        return self.pv_record_map.hdfm_numcapture_rbv
    
    
    @property
    def hdfm_writefile(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFM_WriteFile`."""    
        return self.pv_record_map.hdfm_writefile
    
    
    @property
    def hdfm_writefile_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFM_WriteFile_RBV`."""    
        return self.pv_record_map.hdfm_writefile_rbv
    
    
    @property
    def hdfm_writemessage(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFM_WriteMessage`."""    
        return self.pv_record_map.hdfm_writemessage
    
    
    @property
    def hdfm_writestatus(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDFM_WriteStatus`."""    
        return self.pv_record_map.hdfm_writestatus
    
    
    @property
    def hdf_autosave(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDF_AutoSave`."""    
        return self.pv_record_map.hdf_autosave
    
    @hdf_autosave.setter
    def hdf_autosave(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.HDF_AutoSave`.""" 
        self.pv_record_map.hdf_autosave = value
    
    
    @property
    def hdf_capture(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDF_Capture`."""    
        return self.pv_record_map.hdf_capture
    
    @hdf_capture.setter
    def hdf_capture(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.HDF_Capture`.""" 
        self.pv_record_map.hdf_capture = value
    
    
    @property
    def hdf_capture_disv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDF_Capture_DISV`."""    
        return self.pv_record_map.hdf_capture_disv
    
    @hdf_capture_disv.setter
    def hdf_capture_disv(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.HDF_Capture_DISV`.""" 
        self.pv_record_map.hdf_capture_disv = value
    
    
    @property
    def hdf_capture_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDF_Capture_RBV`."""    
        return self.pv_record_map.hdf_capture_rbv
    
    
    @property
    def hdf_filename(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDF_FileName`."""    
        return self.pv_record_map.hdf_filename
    
    
    @property
    def hdf_filename_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDF_FileName_RBV`."""    
        return self.pv_record_map.hdf_filename_rbv
    
    
    @property
    def hdf_filenumber(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDF_FileNumber`."""    
        return self.pv_record_map.hdf_filenumber
    
    
    @property
    def hdf_filenumber_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDF_FileNumber_RBV`."""    
        return self.pv_record_map.hdf_filenumber_rbv
    
    
    @property
    def hdf_filepath(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDF_FilePath`."""    
        return self.pv_record_map.hdf_filepath
    
    
    @property
    def hdf_filepath_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDF_FilePath_RBV`."""    
        return self.pv_record_map.hdf_filepath_rbv
    
    
    @property
    def hdf_filewritemode(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDF_FileWriteMode`."""    
        return self.pv_record_map.hdf_filewritemode
    
    @hdf_filewritemode.setter
    def hdf_filewritemode(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.HDF_FileWriteMode`.""" 
        self.pv_record_map.hdf_filewritemode = value
    
    
    @property
    def hdf_numcapture(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDF_NumCapture`."""    
        return self.pv_record_map.hdf_numcapture
    
    @hdf_numcapture.setter
    def hdf_numcapture(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.HDF_NumCapture`.""" 
        self.pv_record_map.hdf_numcapture = value
    
    
    @property
    def hdf_numcapture_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDF_NumCapture_RBV`."""    
        return self.pv_record_map.hdf_numcapture_rbv
    
    
    @property
    def hdf_writefile(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDF_WriteFile`."""    
        return self.pv_record_map.hdf_writefile
    
    
    @property
    def hdf_writefile_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDF_WriteFile_RBV`."""    
        return self.pv_record_map.hdf_writefile_rbv
    
    
    @property
    def hdf_writemessage(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDF_WriteMessage`."""    
        return self.pv_record_map.hdf_writemessage
    
    
    @property
    def hdf_writestatus(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.HDF_WriteStatus`."""    
        return self.pv_record_map.hdf_writestatus
    
    
    @property
    def init_buffer(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.Init_Buffer`."""    
        return self.pv_record_map.init_buffer
    
    @init_buffer.setter
    def init_buffer(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.Init_Buffer`.""" 
        self.pv_record_map.init_buffer = value
    
    
    @property
    def led_off(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.LED_Off`."""    
        return self.pv_record_map.led_off
    
    @led_off.setter
    def led_off(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.LED_Off`.""" 
        self.pv_record_map.led_off = value
    
    
    @property
    def led_on(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.LED_On`."""    
        return self.pv_record_map.led_on
    
    @led_on.setter
    def led_on(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.LED_On`.""" 
        self.pv_record_map.led_on = value
    
    
    @property
    def led_sta(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.LED_Sta`."""    
        return self.pv_record_map.led_sta
    
    
    @property
    def magick_autosave(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.MAGICK_AutoSave`."""    
        return self.pv_record_map.magick_autosave
    
    @magick_autosave.setter
    def magick_autosave(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.MAGICK_AutoSave`.""" 
        self.pv_record_map.magick_autosave = value
    
    
    @property
    def magick_capture(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.MAGICK_Capture`."""    
        return self.pv_record_map.magick_capture
    
    @magick_capture.setter
    def magick_capture(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.MAGICK_Capture`.""" 
        self.pv_record_map.magick_capture = value
    
    
    @property
    def magick_capture_disv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.MAGICK_Capture_DISV`."""    
        return self.pv_record_map.magick_capture_disv
    
    @magick_capture_disv.setter
    def magick_capture_disv(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.MAGICK_Capture_DISV`.""" 
        self.pv_record_map.magick_capture_disv = value
    
    
    @property
    def magick_capture_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.MAGICK_Capture_RBV`."""    
        return self.pv_record_map.magick_capture_rbv
    
    
    @property
    def magick_filename(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.MAGICK_FileName`."""    
        return self.pv_record_map.magick_filename
    
    
    @property
    def magick_filename_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.MAGICK_FileName_RBV`."""    
        return self.pv_record_map.magick_filename_rbv
    
    
    @property
    def magick_filenumber(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.MAGICK_FileNumber`."""    
        return self.pv_record_map.magick_filenumber
    
    
    @property
    def magick_filenumber_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.MAGICK_FileNumber_RBV`."""    
        return self.pv_record_map.magick_filenumber_rbv
    
    
    @property
    def magick_filepath(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.MAGICK_FilePath`."""    
        return self.pv_record_map.magick_filepath
    
    
    @property
    def magick_filepath_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.MAGICK_FilePath_RBV`."""    
        return self.pv_record_map.magick_filepath_rbv
    
    
    @property
    def magick_filewritemode(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.MAGICK_FileWriteMode`."""    
        return self.pv_record_map.magick_filewritemode
    
    @magick_filewritemode.setter
    def magick_filewritemode(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.MAGICK_FileWriteMode`.""" 
        self.pv_record_map.magick_filewritemode = value
    
    
    @property
    def magick_numcapture(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.MAGICK_NumCapture`."""    
        return self.pv_record_map.magick_numcapture
    
    @magick_numcapture.setter
    def magick_numcapture(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.MAGICK_NumCapture`.""" 
        self.pv_record_map.magick_numcapture = value
    
    
    @property
    def magick_numcapture_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.MAGICK_NumCapture_RBV`."""    
        return self.pv_record_map.magick_numcapture_rbv
    
    
    @property
    def magick_writefile(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.MAGICK_WriteFile`."""    
        return self.pv_record_map.magick_writefile
    
    
    @property
    def magick_writefile_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.MAGICK_WriteFile_RBV`."""    
        return self.pv_record_map.magick_writefile_rbv
    
    
    @property
    def magick_writemessage(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.MAGICK_WriteMessage`."""    
        return self.pv_record_map.magick_writemessage
    
    
    @property
    def magick_writestatus(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.MAGICK_WriteStatus`."""    
        return self.pv_record_map.magick_writestatus
    
    
    @property
    def roi1_imagedata_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ROI1_ImageData_RBV`."""    
        return self.pv_record_map.roi1_imagedata_rbv
    
    
    @property
    def roi1_minx(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ROI1_MinX`."""    
        return self.pv_record_map.roi1_minx
    
    
    @property
    def roi1_minx_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ROI1_MinX_RBV`."""    
        return self.pv_record_map.roi1_minx_rbv
    
    
    @property
    def roi1_miny(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ROI1_MinY`."""    
        return self.pv_record_map.roi1_miny
    
    
    @property
    def roi1_miny_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ROI1_MinY_RBV`."""    
        return self.pv_record_map.roi1_miny_rbv
    
    
    @property
    def roi1_sizex(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ROI1_SizeX`."""    
        return self.pv_record_map.roi1_sizex
    
    
    @property
    def roi1_sizex_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ROI1_SizeX_RBV`."""    
        return self.pv_record_map.roi1_sizex_rbv
    
    
    @property
    def roi1_sizey(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ROI1_SizeY`."""    
        return self.pv_record_map.roi1_sizey
    
    
    @property
    def roi1_sizey_rbv(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ROI1_SizeY_RBV`."""    
        return self.pv_record_map.roi1_sizey_rbv
    
    
    @property
    def roiandmask_setx(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ROIandMask_SetX`."""    
        return self.pv_record_map.roiandmask_setx
    
    
    @property
    def roiandmask_setxrad(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ROIandMask_SetXrad`."""    
        return self.pv_record_map.roiandmask_setxrad
    
    
    @property
    def roiandmask_sety(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ROIandMask_SetY`."""    
        return self.pv_record_map.roiandmask_sety
    
    
    @property
    def roiandmask_setyrad(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.ROIandMask_SetYrad`."""    
        return self.pv_record_map.roiandmask_setyrad
    
    
    @property
    def reset_buffer(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.Reset_Buffer`."""    
        return self.pv_record_map.reset_buffer
    
    @reset_buffer.setter
    def reset_buffer(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.Reset_Buffer`.""" 
        self.pv_record_map.reset_buffer = value
    
    
    @property
    def save(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.Save`."""    
        return self.pv_record_map.save
    
    @save.setter
    def save(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.Save`.""" 
        self.pv_record_map.save = value
    
    
    @property
    def save_buffer(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.Save_Buffer`."""    
        return self.pv_record_map.save_buffer
    
    @save_buffer.setter
    def save_buffer(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.Save_Buffer`.""" 
        self.pv_record_map.save_buffer = value
    
    
    @property
    def save_buffer_path_initialise(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.Save_Buffer_Path_Initialise`."""    
        return self.pv_record_map.save_buffer_path_initialise
    
    @save_buffer_path_initialise.setter
    def save_buffer_path_initialise(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.Save_Buffer_Path_Initialise`.""" 
        self.pv_record_map.save_buffer_path_initialise = value
    
    
    @property
    def save_path_initialise(self):
        """Default Getter implementation for :attr:`CameraPVMapModel.Save_Path_Initialise`."""    
        return self.pv_record_map.save_path_initialise
    
    @save_path_initialise.setter
    def save_path_initialise(self, value):
        """Default Setter implementation for :attr:`CameraPVMapModel.Save_Path_Initialise`.""" 
        self.pv_record_map.save_path_initialise = value
    
    

    


class CameraPropertiesModel(Properties):
    """
    Class for defining camera-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """
    
    
    type: str
    
    
    
    ARRAY_DATA_NUM_PIX_X: int
    
    
    
    ARRAY_DATA_NUM_PIX_Y: int
    
    
    
    ARRAY_DATA_X_PIX_2_MM: float
    
    
    
    ARRAY_DATA_Y_PIX_2_MM: float
    
    
    
    HAS_LED: bool
    
    
    
    IMAGE_FLIP_LR: bool
    
    
    
    IMAGE_FLIP_UD: bool
    
    
    
    IMAGE_ROTATION: int
    
    
    
    IOC: list
    
    
    
    IP_ADDRESS_STREAM: Any
    
    
    
    MAX_BIT_DEPTH: int
    
    
    
    PIX_2_MM_RATIO_DEF: float
    
    
    
    SCREEN_NAME: str
    
    
    
    USE_MASK_RAD_LIMITS: bool
    
    
    
    timeout: float
    
    

    def __init__(self, *args, **kwargs):
        super(
            CameraPropertiesModel,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

class CameraModel(Hardware):
    """
    Middle layer class for interacting with a specific camera object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[CameraControlsInformationModel]
    """Controls information pertaining to this camera
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[CameraPropertiesModel]
    """Properties pertaining to this camera
    (see :class:`~CATAP.common.machine.pv_utils.Properties`)"""

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        super(
            CameraModel,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )
        self._snapshot_settables = []
        self._snapshot_gettables = [
            
        ]

    @field_validator("controls_information", mode="before")
    @classmethod
    def validate_controls_information(cls, v: Any) -> CameraControlsInformationModel:
        try:
            return CameraControlsInformationModel(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> CameraPropertiesModel:
        try:
            return CameraPropertiesModel(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def ana_avgintensity_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_AvgIntensity_RBV`."""
        return self.controls_information.ana_avgintensity_rbv
    
    
    @property
    def ana_cpu_cropsubmask_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_CPU_CropSubMask_RBV`."""
        return self.controls_information.ana_cpu_cropsubmask_rbv
    
    
    @property
    def ana_cpu_dot_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_CPU_Dot_RBV`."""
        return self.controls_information.ana_cpu_dot_rbv
    
    
    @property
    def ana_cpu_npoint_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_CPU_Npoint_RBV`."""
        return self.controls_information.ana_cpu_npoint_rbv
    
    
    @property
    def ana_cpu_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_CPU_RBV`."""
        return self.controls_information.ana_cpu_rbv
    
    
    @property
    def ana_centerx(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_CenterX`."""
        return self.controls_information.ana_centerx
    
    
    @property
    def ana_centerx_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_CenterX_RBV`."""
        return self.controls_information.ana_centerx_rbv
    
    
    @property
    def ana_centery(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_CenterY`."""
        return self.controls_information.ana_centery
    
    
    @property
    def ana_centery_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_CenterY_RBV`."""
        return self.controls_information.ana_centery_rbv
    
    
    @property
    def ana_covxypix_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_CovXYPix_RBV`."""
        return self.controls_information.ana_covxypix_rbv
    
    
    @property
    def ana_covxy_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_CovXY_RBV`."""
        return self.controls_information.ana_covxy_rbv
    
    
    @property
    def ana_enablecallbacks(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_EnableCallbacks`."""
        return self.controls_information.ana_enablecallbacks
    
    @ana_enablecallbacks.setter
    def ana_enablecallbacks(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.ANA_EnableCallbacks`."""
        self.controls_information.ana_enablecallbacks = value
    
    
    @property
    def ana_enablecallbacks_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_EnableCallbacks_RBV`."""
        return self.controls_information.ana_enablecallbacks_rbv
    
    
    @property
    def ana_floorlevel(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_FloorLevel`."""
        return self.controls_information.ana_floorlevel
    
    
    @property
    def ana_floorlevel_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_FloorLevel_RBV`."""
        return self.controls_information.ana_floorlevel_rbv
    
    
    @property
    def ana_flooredpercent_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_FlooredPercent_RBV`."""
        return self.controls_information.ana_flooredpercent_rbv
    
    
    @property
    def ana_flooredpoints_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_FlooredPoints_RBV`."""
        return self.controls_information.ana_flooredpoints_rbv
    
    
    @property
    def ana_intensity_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_Intensity_RBV`."""
        return self.controls_information.ana_intensity_rbv
    
    
    @property
    def ana_mmresults_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_MMResults_RBV`."""
        return self.controls_information.ana_mmresults_rbv
    
    
    @property
    def ana_maskheight_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_MaskHeight_RBV`."""
        return self.controls_information.ana_maskheight_rbv
    
    
    @property
    def ana_maskwidth_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_MaskWidth_RBV`."""
        return self.controls_information.ana_maskwidth_rbv
    
    
    @property
    def ana_maskxcenter(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_MaskXCenter`."""
        return self.controls_information.ana_maskxcenter
    
    
    @property
    def ana_maskxcenter_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_MaskXCenter_RBV`."""
        return self.controls_information.ana_maskxcenter_rbv
    
    
    @property
    def ana_maskxrad(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_MaskXRad`."""
        return self.controls_information.ana_maskxrad
    
    
    @property
    def ana_maskxrad_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_MaskXRad_RBV`."""
        return self.controls_information.ana_maskxrad_rbv
    
    
    @property
    def ana_maskycenter(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_MaskYCenter`."""
        return self.controls_information.ana_maskycenter
    
    
    @property
    def ana_maskycenter_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_MaskYCenter_RBV`."""
        return self.controls_information.ana_maskycenter_rbv
    
    
    @property
    def ana_maskyrad(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_MaskYRad`."""
        return self.controls_information.ana_maskyrad
    
    
    @property
    def ana_maskyrad_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_MaskYRad_RBV`."""
        return self.controls_information.ana_maskyrad_rbv
    
    
    @property
    def ana_npointstepsize(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_NPointStepSize`."""
        return self.controls_information.ana_npointstepsize
    
    
    @property
    def ana_npointstepsize_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_NPointStepSize_RBV`."""
        return self.controls_information.ana_npointstepsize_rbv
    
    
    @property
    def ana_newbkgrnd(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_NewBkgrnd`."""
        return self.controls_information.ana_newbkgrnd
    
    
    @property
    def ana_newbkgrnd_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_NewBkgrnd_RBV`."""
        return self.controls_information.ana_newbkgrnd_rbv
    
    
    @property
    def ana_overlay_1_cross(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_OVERLAY_1_CROSS`."""
        return self.controls_information.ana_overlay_1_cross
    
    
    @property
    def ana_overlay_1_cross_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_OVERLAY_1_CROSS_RBV`."""
        return self.controls_information.ana_overlay_1_cross_rbv
    
    
    @property
    def ana_overlay_2_result(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_OVERLAY_2_RESULT`."""
        return self.controls_information.ana_overlay_2_result
    
    
    @property
    def ana_overlay_2_result_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_OVERLAY_2_RESULT_RBV`."""
        return self.controls_information.ana_overlay_2_result_rbv
    
    
    @property
    def ana_overlay_3_mask(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_OVERLAY_3_MASK`."""
        return self.controls_information.ana_overlay_3_mask
    
    
    @property
    def ana_overlay_3_mask_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_OVERLAY_3_MASK_RBV`."""
        return self.controls_information.ana_overlay_3_mask_rbv
    
    
    @property
    def ana_pixh_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_PixH_RBV`."""
        return self.controls_information.ana_pixh_rbv
    
    
    @property
    def ana_pixmm(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_PixMM`."""
        return self.controls_information.ana_pixmm
    
    
    @property
    def ana_pixmm_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_PixMM_RBV`."""
        return self.controls_information.ana_pixmm_rbv
    
    
    @property
    def ana_pixw_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_PixW_RBV`."""
        return self.controls_information.ana_pixw_rbv
    
    
    @property
    def ana_pixelresults_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_PixelResults_RBV`."""
        return self.controls_information.ana_pixelresults_rbv
    
    
    @property
    def ana_sigmaxpix_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_SigmaXPix_RBV`."""
        return self.controls_information.ana_sigmaxpix_rbv
    
    
    @property
    def ana_sigmax_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_SigmaX_RBV`."""
        return self.controls_information.ana_sigmax_rbv
    
    
    @property
    def ana_sigmaypix_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_SigmaYPix_RBV`."""
        return self.controls_information.ana_sigmaypix_rbv
    
    
    @property
    def ana_sigmay_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_SigmaY_RBV`."""
        return self.controls_information.ana_sigmay_rbv
    
    
    @property
    def ana_usebkgrnd(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_UseBkgrnd`."""
        return self.controls_information.ana_usebkgrnd
    
    
    @property
    def ana_usebkgrnd_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_UseBkgrnd_RBV`."""
        return self.controls_information.ana_usebkgrnd_rbv
    
    
    @property
    def ana_usefloor(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_UseFloor`."""
        return self.controls_information.ana_usefloor
    
    
    @property
    def ana_usefloor_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_UseFloor_RBV`."""
        return self.controls_information.ana_usefloor_rbv
    
    
    @property
    def ana_usenpoint(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_UseNPoint`."""
        return self.controls_information.ana_usenpoint
    
    
    @property
    def ana_usenpoint_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_UseNPoint_RBV`."""
        return self.controls_information.ana_usenpoint_rbv
    
    
    @property
    def ana_xpix_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_XPix_RBV`."""
        return self.controls_information.ana_xpix_rbv
    
    
    @property
    def ana_x_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_X_RBV`."""
        return self.controls_information.ana_x_rbv
    
    
    @property
    def ana_ypix_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_YPix_RBV`."""
        return self.controls_information.ana_ypix_rbv
    
    
    @property
    def ana_y_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ANA_Y_RBV`."""
        return self.controls_information.ana_y_rbv
    
    
    @property
    def buffer_status(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.Buffer_Status`."""
        return self.controls_information.buffer_status
    
    
    @property
    def cam1_arraydata(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.CAM1_ArrayData`."""
        return self.controls_information.cam1_arraydata
    
    
    @property
    def cam2_arraydata(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.CAM2_ArrayData`."""
        return self.controls_information.cam2_arraydata
    
    
    @property
    def cam_acquireperiod_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.CAM_AcquirePeriod_RBV`."""
        return self.controls_information.cam_acquireperiod_rbv
    
    
    @property
    def cam_acquiretime_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.CAM_AcquireTime_RBV`."""
        return self.controls_information.cam_acquiretime_rbv
    
    
    @property
    def cam_acquire_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.CAM_Acquire_RBV`."""
        return self.controls_information.cam_acquire_rbv
    
    
    @property
    def cam_active_count(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.CAM_Active_Count`."""
        return self.controls_information.cam_active_count
    
    
    @property
    def cam_active_limit(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.CAM_Active_Limit`."""
        return self.controls_information.cam_active_limit
    
    
    @property
    def cam_arrayrate_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.CAM_ArrayRate_RBV`."""
        return self.controls_information.cam_arrayrate_rbv
    
    
    @property
    def cam_start_acquire(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.CAM_Start_Acquire`."""
        return self.controls_information.cam_start_acquire
    
    @cam_start_acquire.setter
    def cam_start_acquire(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.CAM_Start_Acquire`."""
        self.controls_information.cam_start_acquire = value
    
    
    @property
    def cam_stop_acquire(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.CAM_Stop_Acquire`."""
        return self.controls_information.cam_stop_acquire
    
    @cam_stop_acquire.setter
    def cam_stop_acquire(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.CAM_Stop_Acquire`."""
        self.controls_information.cam_stop_acquire = value
    
    
    @property
    def cam_temperature_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.CAM_Temperature_RBV`."""
        return self.controls_information.cam_temperature_rbv
    
    
    @property
    def hdfb_autosave(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_AutoSave`."""
        return self.controls_information.hdfb_autosave
    
    @hdfb_autosave.setter
    def hdfb_autosave(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.HDFB_AutoSave`."""
        self.controls_information.hdfb_autosave = value
    
    
    @property
    def hdfb_buffer_filenumber(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_Buffer_FileNumber`."""
        return self.controls_information.hdfb_buffer_filenumber
    
    
    @property
    def hdfb_buffer_filenumber_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_Buffer_FileNumber_RBV`."""
        return self.controls_information.hdfb_buffer_filenumber_rbv
    
    
    @property
    def hdfb_capture(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_Capture`."""
        return self.controls_information.hdfb_capture
    
    @hdfb_capture.setter
    def hdfb_capture(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.HDFB_Capture`."""
        self.controls_information.hdfb_capture = value
    
    
    @property
    def hdfb_capture_disv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_Capture_DISV`."""
        return self.controls_information.hdfb_capture_disv
    
    @hdfb_capture_disv.setter
    def hdfb_capture_disv(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.HDFB_Capture_DISV`."""
        self.controls_information.hdfb_capture_disv = value
    
    
    @property
    def hdfb_capture_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_Capture_RBV`."""
        return self.controls_information.hdfb_capture_rbv
    
    
    @property
    def hdfb_filename(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_FileName`."""
        return self.controls_information.hdfb_filename
    
    
    @property
    def hdfb_filename_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_FileName_RBV`."""
        return self.controls_information.hdfb_filename_rbv
    
    
    @property
    def hdfb_filenumber(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_FileNumber`."""
        return self.controls_information.hdfb_filenumber
    
    
    @property
    def hdfb_filenumber_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_FileNumber_RBV`."""
        return self.controls_information.hdfb_filenumber_rbv
    
    
    @property
    def hdfb_filepath(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_FilePath`."""
        return self.controls_information.hdfb_filepath
    
    
    @property
    def hdfb_filepath_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_FilePath_RBV`."""
        return self.controls_information.hdfb_filepath_rbv
    
    
    @property
    def hdfb_filewritemode(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_FileWriteMode`."""
        return self.controls_information.hdfb_filewritemode
    
    @hdfb_filewritemode.setter
    def hdfb_filewritemode(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.HDFB_FileWriteMode`."""
        self.controls_information.hdfb_filewritemode = value
    
    
    @property
    def hdfb_numcapture(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_NumCapture`."""
        return self.controls_information.hdfb_numcapture
    
    @hdfb_numcapture.setter
    def hdfb_numcapture(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.HDFB_NumCapture`."""
        self.controls_information.hdfb_numcapture = value
    
    
    @property
    def hdfb_numcapture_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_NumCapture_RBV`."""
        return self.controls_information.hdfb_numcapture_rbv
    
    
    @property
    def hdfb_numcaptured_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_NumCaptured_RBV`."""
        return self.controls_information.hdfb_numcaptured_rbv
    
    
    @property
    def hdfb_numimagescached_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_NumImagesCached_RBV`."""
        return self.controls_information.hdfb_numimagescached_rbv
    
    
    @property
    def hdfb_postcount(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_PostCount`."""
        return self.controls_information.hdfb_postcount
    
    @hdfb_postcount.setter
    def hdfb_postcount(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.HDFB_PostCount`."""
        self.controls_information.hdfb_postcount = value
    
    
    @property
    def hdfb_precount(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_PreCount`."""
        return self.controls_information.hdfb_precount
    
    @hdfb_precount.setter
    def hdfb_precount(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.HDFB_PreCount`."""
        self.controls_information.hdfb_precount = value
    
    
    @property
    def hdfb_writefile(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_WriteFile`."""
        return self.controls_information.hdfb_writefile
    
    
    @property
    def hdfb_writefile_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_WriteFile_RBV`."""
        return self.controls_information.hdfb_writefile_rbv
    
    
    @property
    def hdfb_writemessage(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_WriteMessage`."""
        return self.controls_information.hdfb_writemessage
    
    
    @property
    def hdfb_writestatus(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_WriteStatus`."""
        return self.controls_information.hdfb_writestatus
    
    
    @property
    def hdfb_image_buffer_filename(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_image_buffer_fileName`."""
        return self.controls_information.hdfb_image_buffer_filename
    
    
    @property
    def hdfb_image_buffer_filename_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_image_buffer_fileName_RBV`."""
        return self.controls_information.hdfb_image_buffer_filename_rbv
    
    
    @property
    def hdfb_image_buffer_filepath(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_image_buffer_filePath`."""
        return self.controls_information.hdfb_image_buffer_filepath
    
    
    @property
    def hdfb_image_buffer_filepath_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_image_buffer_filePath_RBV`."""
        return self.controls_information.hdfb_image_buffer_filepath_rbv
    
    
    @property
    def hdfb_image_buffer_trigger(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFB_image_buffer_trigger`."""
        return self.controls_information.hdfb_image_buffer_trigger
    
    
    @property
    def hdfm_autosave(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFM_AutoSave`."""
        return self.controls_information.hdfm_autosave
    
    @hdfm_autosave.setter
    def hdfm_autosave(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.HDFM_AutoSave`."""
        self.controls_information.hdfm_autosave = value
    
    
    @property
    def hdfm_capture(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFM_Capture`."""
        return self.controls_information.hdfm_capture
    
    @hdfm_capture.setter
    def hdfm_capture(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.HDFM_Capture`."""
        self.controls_information.hdfm_capture = value
    
    
    @property
    def hdfm_capture_disv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFM_Capture_DISV`."""
        return self.controls_information.hdfm_capture_disv
    
    @hdfm_capture_disv.setter
    def hdfm_capture_disv(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.HDFM_Capture_DISV`."""
        self.controls_information.hdfm_capture_disv = value
    
    
    @property
    def hdfm_capture_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFM_Capture_RBV`."""
        return self.controls_information.hdfm_capture_rbv
    
    
    @property
    def hdfm_filename(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFM_FileName`."""
        return self.controls_information.hdfm_filename
    
    
    @property
    def hdfm_filename_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFM_FileName_RBV`."""
        return self.controls_information.hdfm_filename_rbv
    
    
    @property
    def hdfm_filenumber(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFM_FileNumber`."""
        return self.controls_information.hdfm_filenumber
    
    
    @property
    def hdfm_filenumber_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFM_FileNumber_RBV`."""
        return self.controls_information.hdfm_filenumber_rbv
    
    
    @property
    def hdfm_filepath(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFM_FilePath`."""
        return self.controls_information.hdfm_filepath
    
    
    @property
    def hdfm_filepath_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFM_FilePath_RBV`."""
        return self.controls_information.hdfm_filepath_rbv
    
    
    @property
    def hdfm_filewritemode(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFM_FileWriteMode`."""
        return self.controls_information.hdfm_filewritemode
    
    @hdfm_filewritemode.setter
    def hdfm_filewritemode(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.HDFM_FileWriteMode`."""
        self.controls_information.hdfm_filewritemode = value
    
    
    @property
    def hdfm_numcapture(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFM_NumCapture`."""
        return self.controls_information.hdfm_numcapture
    
    @hdfm_numcapture.setter
    def hdfm_numcapture(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.HDFM_NumCapture`."""
        self.controls_information.hdfm_numcapture = value
    
    
    @property
    def hdfm_numcapture_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFM_NumCapture_RBV`."""
        return self.controls_information.hdfm_numcapture_rbv
    
    
    @property
    def hdfm_writefile(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFM_WriteFile`."""
        return self.controls_information.hdfm_writefile
    
    
    @property
    def hdfm_writefile_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFM_WriteFile_RBV`."""
        return self.controls_information.hdfm_writefile_rbv
    
    
    @property
    def hdfm_writemessage(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFM_WriteMessage`."""
        return self.controls_information.hdfm_writemessage
    
    
    @property
    def hdfm_writestatus(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDFM_WriteStatus`."""
        return self.controls_information.hdfm_writestatus
    
    
    @property
    def hdf_autosave(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDF_AutoSave`."""
        return self.controls_information.hdf_autosave
    
    @hdf_autosave.setter
    def hdf_autosave(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.HDF_AutoSave`."""
        self.controls_information.hdf_autosave = value
    
    
    @property
    def hdf_capture(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDF_Capture`."""
        return self.controls_information.hdf_capture
    
    @hdf_capture.setter
    def hdf_capture(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.HDF_Capture`."""
        self.controls_information.hdf_capture = value
    
    
    @property
    def hdf_capture_disv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDF_Capture_DISV`."""
        return self.controls_information.hdf_capture_disv
    
    @hdf_capture_disv.setter
    def hdf_capture_disv(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.HDF_Capture_DISV`."""
        self.controls_information.hdf_capture_disv = value
    
    
    @property
    def hdf_capture_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDF_Capture_RBV`."""
        return self.controls_information.hdf_capture_rbv
    
    
    @property
    def hdf_filename(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDF_FileName`."""
        return self.controls_information.hdf_filename
    
    
    @property
    def hdf_filename_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDF_FileName_RBV`."""
        return self.controls_information.hdf_filename_rbv
    
    
    @property
    def hdf_filenumber(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDF_FileNumber`."""
        return self.controls_information.hdf_filenumber
    
    
    @property
    def hdf_filenumber_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDF_FileNumber_RBV`."""
        return self.controls_information.hdf_filenumber_rbv
    
    
    @property
    def hdf_filepath(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDF_FilePath`."""
        return self.controls_information.hdf_filepath
    
    
    @property
    def hdf_filepath_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDF_FilePath_RBV`."""
        return self.controls_information.hdf_filepath_rbv
    
    
    @property
    def hdf_filewritemode(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDF_FileWriteMode`."""
        return self.controls_information.hdf_filewritemode
    
    @hdf_filewritemode.setter
    def hdf_filewritemode(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.HDF_FileWriteMode`."""
        self.controls_information.hdf_filewritemode = value
    
    
    @property
    def hdf_numcapture(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDF_NumCapture`."""
        return self.controls_information.hdf_numcapture
    
    @hdf_numcapture.setter
    def hdf_numcapture(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.HDF_NumCapture`."""
        self.controls_information.hdf_numcapture = value
    
    
    @property
    def hdf_numcapture_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDF_NumCapture_RBV`."""
        return self.controls_information.hdf_numcapture_rbv
    
    
    @property
    def hdf_writefile(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDF_WriteFile`."""
        return self.controls_information.hdf_writefile
    
    
    @property
    def hdf_writefile_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDF_WriteFile_RBV`."""
        return self.controls_information.hdf_writefile_rbv
    
    
    @property
    def hdf_writemessage(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDF_WriteMessage`."""
        return self.controls_information.hdf_writemessage
    
    
    @property
    def hdf_writestatus(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.HDF_WriteStatus`."""
        return self.controls_information.hdf_writestatus
    
    
    @property
    def init_buffer(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.Init_Buffer`."""
        return self.controls_information.init_buffer
    
    @init_buffer.setter
    def init_buffer(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.Init_Buffer`."""
        self.controls_information.init_buffer = value
    
    
    @property
    def led_off(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.LED_Off`."""
        return self.controls_information.led_off
    
    @led_off.setter
    def led_off(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.LED_Off`."""
        self.controls_information.led_off = value
    
    
    @property
    def led_on(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.LED_On`."""
        return self.controls_information.led_on
    
    @led_on.setter
    def led_on(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.LED_On`."""
        self.controls_information.led_on = value
    
    
    @property
    def led_sta(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.LED_Sta`."""
        return self.controls_information.led_sta
    
    
    @property
    def magick_autosave(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.MAGICK_AutoSave`."""
        return self.controls_information.magick_autosave
    
    @magick_autosave.setter
    def magick_autosave(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.MAGICK_AutoSave`."""
        self.controls_information.magick_autosave = value
    
    
    @property
    def magick_capture(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.MAGICK_Capture`."""
        return self.controls_information.magick_capture
    
    @magick_capture.setter
    def magick_capture(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.MAGICK_Capture`."""
        self.controls_information.magick_capture = value
    
    
    @property
    def magick_capture_disv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.MAGICK_Capture_DISV`."""
        return self.controls_information.magick_capture_disv
    
    @magick_capture_disv.setter
    def magick_capture_disv(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.MAGICK_Capture_DISV`."""
        self.controls_information.magick_capture_disv = value
    
    
    @property
    def magick_capture_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.MAGICK_Capture_RBV`."""
        return self.controls_information.magick_capture_rbv
    
    
    @property
    def magick_filename(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.MAGICK_FileName`."""
        return self.controls_information.magick_filename
    
    
    @property
    def magick_filename_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.MAGICK_FileName_RBV`."""
        return self.controls_information.magick_filename_rbv
    
    
    @property
    def magick_filenumber(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.MAGICK_FileNumber`."""
        return self.controls_information.magick_filenumber
    
    
    @property
    def magick_filenumber_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.MAGICK_FileNumber_RBV`."""
        return self.controls_information.magick_filenumber_rbv
    
    
    @property
    def magick_filepath(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.MAGICK_FilePath`."""
        return self.controls_information.magick_filepath
    
    
    @property
    def magick_filepath_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.MAGICK_FilePath_RBV`."""
        return self.controls_information.magick_filepath_rbv
    
    
    @property
    def magick_filewritemode(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.MAGICK_FileWriteMode`."""
        return self.controls_information.magick_filewritemode
    
    @magick_filewritemode.setter
    def magick_filewritemode(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.MAGICK_FileWriteMode`."""
        self.controls_information.magick_filewritemode = value
    
    
    @property
    def magick_numcapture(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.MAGICK_NumCapture`."""
        return self.controls_information.magick_numcapture
    
    @magick_numcapture.setter
    def magick_numcapture(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.MAGICK_NumCapture`."""
        self.controls_information.magick_numcapture = value
    
    
    @property
    def magick_numcapture_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.MAGICK_NumCapture_RBV`."""
        return self.controls_information.magick_numcapture_rbv
    
    
    @property
    def magick_writefile(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.MAGICK_WriteFile`."""
        return self.controls_information.magick_writefile
    
    
    @property
    def magick_writefile_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.MAGICK_WriteFile_RBV`."""
        return self.controls_information.magick_writefile_rbv
    
    
    @property
    def magick_writemessage(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.MAGICK_WriteMessage`."""
        return self.controls_information.magick_writemessage
    
    
    @property
    def magick_writestatus(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.MAGICK_WriteStatus`."""
        return self.controls_information.magick_writestatus
    
    
    @property
    def roi1_imagedata_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ROI1_ImageData_RBV`."""
        return self.controls_information.roi1_imagedata_rbv
    
    
    @property
    def roi1_minx(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ROI1_MinX`."""
        return self.controls_information.roi1_minx
    
    
    @property
    def roi1_minx_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ROI1_MinX_RBV`."""
        return self.controls_information.roi1_minx_rbv
    
    
    @property
    def roi1_miny(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ROI1_MinY`."""
        return self.controls_information.roi1_miny
    
    
    @property
    def roi1_miny_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ROI1_MinY_RBV`."""
        return self.controls_information.roi1_miny_rbv
    
    
    @property
    def roi1_sizex(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ROI1_SizeX`."""
        return self.controls_information.roi1_sizex
    
    
    @property
    def roi1_sizex_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ROI1_SizeX_RBV`."""
        return self.controls_information.roi1_sizex_rbv
    
    
    @property
    def roi1_sizey(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ROI1_SizeY`."""
        return self.controls_information.roi1_sizey
    
    
    @property
    def roi1_sizey_rbv(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ROI1_SizeY_RBV`."""
        return self.controls_information.roi1_sizey_rbv
    
    
    @property
    def roiandmask_setx(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ROIandMask_SetX`."""
        return self.controls_information.roiandmask_setx
    
    
    @property
    def roiandmask_setxrad(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ROIandMask_SetXrad`."""
        return self.controls_information.roiandmask_setxrad
    
    
    @property
    def roiandmask_sety(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ROIandMask_SetY`."""
        return self.controls_information.roiandmask_sety
    
    
    @property
    def roiandmask_setyrad(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.ROIandMask_SetYrad`."""
        return self.controls_information.roiandmask_setyrad
    
    
    @property
    def reset_buffer(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.Reset_Buffer`."""
        return self.controls_information.reset_buffer
    
    @reset_buffer.setter
    def reset_buffer(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.Reset_Buffer`."""
        self.controls_information.reset_buffer = value
    
    
    @property
    def save(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.Save`."""
        return self.controls_information.save
    
    @save.setter
    def save(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.Save`."""
        self.controls_information.save = value
    
    
    @property
    def save_buffer(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.Save_Buffer`."""
        return self.controls_information.save_buffer
    
    @save_buffer.setter
    def save_buffer(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.Save_Buffer`."""
        self.controls_information.save_buffer = value
    
    
    @property
    def save_buffer_path_initialise(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.Save_Buffer_Path_Initialise`."""
        return self.controls_information.save_buffer_path_initialise
    
    @save_buffer_path_initialise.setter
    def save_buffer_path_initialise(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.Save_Buffer_Path_Initialise`."""
        self.controls_information.save_buffer_path_initialise = value
    
    
    @property
    def save_path_initialise(self):
        """Default Getter implementation for :attr:`CameraControlsInformationModel.Save_Path_Initialise`."""
        return self.controls_information.save_path_initialise
    
    @save_path_initialise.setter
    def save_path_initialise(self, value):
        """Default Setter implementation for :attr:`CameraControlsInformationModel.Save_Path_Initialise`."""
        self.controls_information.save_path_initialise = value
    
    

class CameraFactoryModel(Factory):
    """
    Middle layer class for interacting with multiple
    :class:`CATAP.laser.components.camera.Camera` objects.

    Inherits from:
        :class:`~CATAP.common.machine.factory.Factory`
    """

    def __init__(
        self,
        is_virtual: bool = True,
        connect_on_creation: bool = False,
        areas: Union[MachineArea, List[MachineArea]] = None,
    ):
        super(CameraFactoryModel, self).__init__(
            is_virtual=is_virtual,
            hardware_type=CameraModel,
            lattice_folder="Camera",
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_camera(self, name: Union[str, List[str]] = None) -> CameraModel:
        """
        Returns the camera object for the given name(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str

        :return: Camera object(s).
        :rtype: :class:`cameraModel.Camera`
        or Dict[str: :class:`camera.Camera`]
        """
        return self.get_hardware(name)

    
    def ana_avgintensity_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_AvgIntensity_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_AvgIntensity_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_avgintensity_rbv)
    
    def ana_cpu_cropsubmask_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_CPU_CropSubMask_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_CPU_CropSubMask_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_cpu_cropsubmask_rbv)
    
    def ana_cpu_dot_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_CPU_Dot_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_CPU_Dot_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_cpu_dot_rbv)
    
    def ana_cpu_npoint_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_CPU_Npoint_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_CPU_Npoint_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_cpu_npoint_rbv)
    
    def ana_cpu_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_CPU_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_CPU_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_cpu_rbv)
    
    def ana_centerx(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_CenterX`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_CenterX` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_centerx)
    
    def ana_centerx_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_CenterX_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_CenterX_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_centerx_rbv)
    
    def ana_centery(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_CenterY`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_CenterY` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_centery)
    
    def ana_centery_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_CenterY_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_CenterY_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_centery_rbv)
    
    def ana_covxypix_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_CovXYPix_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_CovXYPix_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_covxypix_rbv)
    
    def ana_covxy_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_CovXY_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_CovXY_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_covxy_rbv)
    
    def ana_enablecallbacks(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_EnableCallbacks`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_EnableCallbacks` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_enablecallbacks)
    
    def ana_enablecallbacks_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_EnableCallbacks_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_EnableCallbacks_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_enablecallbacks_rbv)
    
    def ana_floorlevel(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_FloorLevel`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_FloorLevel` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_floorlevel)
    
    def ana_floorlevel_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_FloorLevel_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_FloorLevel_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_floorlevel_rbv)
    
    def ana_flooredpercent_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_FlooredPercent_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_FlooredPercent_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_flooredpercent_rbv)
    
    def ana_flooredpoints_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_FlooredPoints_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_FlooredPoints_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_flooredpoints_rbv)
    
    def ana_intensity_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_Intensity_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_Intensity_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_intensity_rbv)
    
    def ana_mmresults_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_MMResults_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_MMResults_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_mmresults_rbv)
    
    def ana_maskheight_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_MaskHeight_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_MaskHeight_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_maskheight_rbv)
    
    def ana_maskwidth_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_MaskWidth_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_MaskWidth_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_maskwidth_rbv)
    
    def ana_maskxcenter(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_MaskXCenter`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_MaskXCenter` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_maskxcenter)
    
    def ana_maskxcenter_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_MaskXCenter_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_MaskXCenter_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_maskxcenter_rbv)
    
    def ana_maskxrad(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_MaskXRad`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_MaskXRad` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_maskxrad)
    
    def ana_maskxrad_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_MaskXRad_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_MaskXRad_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_maskxrad_rbv)
    
    def ana_maskycenter(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_MaskYCenter`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_MaskYCenter` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_maskycenter)
    
    def ana_maskycenter_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_MaskYCenter_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_MaskYCenter_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_maskycenter_rbv)
    
    def ana_maskyrad(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_MaskYRad`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_MaskYRad` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_maskyrad)
    
    def ana_maskyrad_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_MaskYRad_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_MaskYRad_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_maskyrad_rbv)
    
    def ana_npointstepsize(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_NPointStepSize`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_NPointStepSize` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_npointstepsize)
    
    def ana_npointstepsize_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_NPointStepSize_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_NPointStepSize_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_npointstepsize_rbv)
    
    def ana_newbkgrnd(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_NewBkgrnd`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_NewBkgrnd` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_newbkgrnd)
    
    def ana_newbkgrnd_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_NewBkgrnd_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_NewBkgrnd_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_newbkgrnd_rbv)
    
    def ana_overlay_1_cross(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_OVERLAY_1_CROSS`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_OVERLAY_1_CROSS` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_overlay_1_cross)
    
    def ana_overlay_1_cross_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_OVERLAY_1_CROSS_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_OVERLAY_1_CROSS_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_overlay_1_cross_rbv)
    
    def ana_overlay_2_result(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_OVERLAY_2_RESULT`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_OVERLAY_2_RESULT` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_overlay_2_result)
    
    def ana_overlay_2_result_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_OVERLAY_2_RESULT_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_OVERLAY_2_RESULT_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_overlay_2_result_rbv)
    
    def ana_overlay_3_mask(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_OVERLAY_3_MASK`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_OVERLAY_3_MASK` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_overlay_3_mask)
    
    def ana_overlay_3_mask_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_OVERLAY_3_MASK_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_OVERLAY_3_MASK_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_overlay_3_mask_rbv)
    
    def ana_pixh_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_PixH_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_PixH_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_pixh_rbv)
    
    def ana_pixmm(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_PixMM`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_PixMM` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_pixmm)
    
    def ana_pixmm_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_PixMM_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_PixMM_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_pixmm_rbv)
    
    def ana_pixw_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_PixW_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_PixW_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_pixw_rbv)
    
    def ana_pixelresults_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_PixelResults_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_PixelResults_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_pixelresults_rbv)
    
    def ana_sigmaxpix_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_SigmaXPix_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_SigmaXPix_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_sigmaxpix_rbv)
    
    def ana_sigmax_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_SigmaX_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_SigmaX_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_sigmax_rbv)
    
    def ana_sigmaypix_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_SigmaYPix_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_SigmaYPix_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_sigmaypix_rbv)
    
    def ana_sigmay_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_SigmaY_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_SigmaY_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_sigmay_rbv)
    
    def ana_usebkgrnd(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_UseBkgrnd`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_UseBkgrnd` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_usebkgrnd)
    
    def ana_usebkgrnd_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_UseBkgrnd_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_UseBkgrnd_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_usebkgrnd_rbv)
    
    def ana_usefloor(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_UseFloor`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_UseFloor` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_usefloor)
    
    def ana_usefloor_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_UseFloor_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_UseFloor_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_usefloor_rbv)
    
    def ana_usenpoint(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_UseNPoint`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_UseNPoint` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_usenpoint)
    
    def ana_usenpoint_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_UseNPoint_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_UseNPoint_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_usenpoint_rbv)
    
    def ana_xpix_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_XPix_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_XPix_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_xpix_rbv)
    
    def ana_x_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_X_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_X_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_x_rbv)
    
    def ana_ypix_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_YPix_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_YPix_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_ypix_rbv)
    
    def ana_y_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ANA_Y_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ANA_Y_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_y_rbv)
    
    def buffer_status(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.Buffer_Status`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.Buffer_Status` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.buffer_status)
    
    def cam1_arraydata(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.CAM1_ArrayData`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.CAM1_ArrayData` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam1_arraydata)
    
    def cam2_arraydata(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.CAM2_ArrayData`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.CAM2_ArrayData` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam2_arraydata)
    
    def cam_acquireperiod_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.CAM_AcquirePeriod_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.CAM_AcquirePeriod_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam_acquireperiod_rbv)
    
    def cam_acquiretime_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.CAM_AcquireTime_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.CAM_AcquireTime_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam_acquiretime_rbv)
    
    def cam_acquire_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.CAM_Acquire_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.CAM_Acquire_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam_acquire_rbv)
    
    def cam_active_count(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.CAM_Active_Count`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.CAM_Active_Count` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam_active_count)
    
    def cam_active_limit(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.CAM_Active_Limit`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.CAM_Active_Limit` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam_active_limit)
    
    def cam_arrayrate_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.CAM_ArrayRate_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.CAM_ArrayRate_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam_arrayrate_rbv)
    
    def cam_start_acquire(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.CAM_Start_Acquire`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.CAM_Start_Acquire` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam_start_acquire)
    
    def cam_stop_acquire(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.CAM_Stop_Acquire`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.CAM_Stop_Acquire` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam_stop_acquire)
    
    def cam_temperature_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.CAM_Temperature_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.CAM_Temperature_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam_temperature_rbv)
    
    def hdfb_autosave(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_AutoSave`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_AutoSave` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_autosave)
    
    def hdfb_buffer_filenumber(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_Buffer_FileNumber`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_Buffer_FileNumber` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_buffer_filenumber)
    
    def hdfb_buffer_filenumber_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_Buffer_FileNumber_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_Buffer_FileNumber_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_buffer_filenumber_rbv)
    
    def hdfb_capture(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_Capture`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_Capture` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_capture)
    
    def hdfb_capture_disv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_Capture_DISV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_Capture_DISV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_capture_disv)
    
    def hdfb_capture_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_Capture_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_Capture_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_capture_rbv)
    
    def hdfb_filename(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_FileName`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_FileName` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_filename)
    
    def hdfb_filename_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_FileName_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_FileName_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_filename_rbv)
    
    def hdfb_filenumber(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_FileNumber`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_FileNumber` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_filenumber)
    
    def hdfb_filenumber_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_FileNumber_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_FileNumber_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_filenumber_rbv)
    
    def hdfb_filepath(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_FilePath`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_FilePath` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_filepath)
    
    def hdfb_filepath_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_FilePath_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_FilePath_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_filepath_rbv)
    
    def hdfb_filewritemode(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_FileWriteMode`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_FileWriteMode` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_filewritemode)
    
    def hdfb_numcapture(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_NumCapture`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_NumCapture` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_numcapture)
    
    def hdfb_numcapture_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_NumCapture_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_NumCapture_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_numcapture_rbv)
    
    def hdfb_numcaptured_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_NumCaptured_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_NumCaptured_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_numcaptured_rbv)
    
    def hdfb_numimagescached_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_NumImagesCached_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_NumImagesCached_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_numimagescached_rbv)
    
    def hdfb_postcount(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_PostCount`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_PostCount` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_postcount)
    
    def hdfb_precount(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_PreCount`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_PreCount` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_precount)
    
    def hdfb_writefile(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_WriteFile`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_WriteFile` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_writefile)
    
    def hdfb_writefile_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_WriteFile_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_WriteFile_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_writefile_rbv)
    
    def hdfb_writemessage(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_WriteMessage`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_WriteMessage` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_writemessage)
    
    def hdfb_writestatus(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_WriteStatus`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_WriteStatus` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_writestatus)
    
    def hdfb_image_buffer_filename(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_image_buffer_fileName`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_image_buffer_fileName` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_image_buffer_filename)
    
    def hdfb_image_buffer_filename_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_image_buffer_fileName_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_image_buffer_fileName_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_image_buffer_filename_rbv)
    
    def hdfb_image_buffer_filepath(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_image_buffer_filePath`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_image_buffer_filePath` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_image_buffer_filepath)
    
    def hdfb_image_buffer_filepath_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_image_buffer_filePath_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_image_buffer_filePath_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_image_buffer_filepath_rbv)
    
    def hdfb_image_buffer_trigger(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFB_image_buffer_trigger`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFB_image_buffer_trigger` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_image_buffer_trigger)
    
    def hdfm_autosave(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFM_AutoSave`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFM_AutoSave` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_autosave)
    
    def hdfm_capture(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFM_Capture`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFM_Capture` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_capture)
    
    def hdfm_capture_disv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFM_Capture_DISV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFM_Capture_DISV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_capture_disv)
    
    def hdfm_capture_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFM_Capture_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFM_Capture_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_capture_rbv)
    
    def hdfm_filename(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFM_FileName`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFM_FileName` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_filename)
    
    def hdfm_filename_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFM_FileName_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFM_FileName_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_filename_rbv)
    
    def hdfm_filenumber(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFM_FileNumber`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFM_FileNumber` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_filenumber)
    
    def hdfm_filenumber_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFM_FileNumber_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFM_FileNumber_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_filenumber_rbv)
    
    def hdfm_filepath(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFM_FilePath`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFM_FilePath` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_filepath)
    
    def hdfm_filepath_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFM_FilePath_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFM_FilePath_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_filepath_rbv)
    
    def hdfm_filewritemode(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFM_FileWriteMode`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFM_FileWriteMode` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_filewritemode)
    
    def hdfm_numcapture(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFM_NumCapture`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFM_NumCapture` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_numcapture)
    
    def hdfm_numcapture_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFM_NumCapture_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFM_NumCapture_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_numcapture_rbv)
    
    def hdfm_writefile(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFM_WriteFile`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFM_WriteFile` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_writefile)
    
    def hdfm_writefile_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFM_WriteFile_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFM_WriteFile_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_writefile_rbv)
    
    def hdfm_writemessage(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFM_WriteMessage`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFM_WriteMessage` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_writemessage)
    
    def hdfm_writestatus(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDFM_WriteStatus`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDFM_WriteStatus` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_writestatus)
    
    def hdf_autosave(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDF_AutoSave`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDF_AutoSave` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_autosave)
    
    def hdf_capture(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDF_Capture`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDF_Capture` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_capture)
    
    def hdf_capture_disv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDF_Capture_DISV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDF_Capture_DISV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_capture_disv)
    
    def hdf_capture_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDF_Capture_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDF_Capture_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_capture_rbv)
    
    def hdf_filename(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDF_FileName`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDF_FileName` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_filename)
    
    def hdf_filename_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDF_FileName_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDF_FileName_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_filename_rbv)
    
    def hdf_filenumber(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDF_FileNumber`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDF_FileNumber` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_filenumber)
    
    def hdf_filenumber_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDF_FileNumber_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDF_FileNumber_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_filenumber_rbv)
    
    def hdf_filepath(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDF_FilePath`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDF_FilePath` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_filepath)
    
    def hdf_filepath_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDF_FilePath_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDF_FilePath_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_filepath_rbv)
    
    def hdf_filewritemode(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDF_FileWriteMode`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDF_FileWriteMode` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_filewritemode)
    
    def hdf_numcapture(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDF_NumCapture`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDF_NumCapture` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_numcapture)
    
    def hdf_numcapture_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDF_NumCapture_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDF_NumCapture_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_numcapture_rbv)
    
    def hdf_writefile(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDF_WriteFile`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDF_WriteFile` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_writefile)
    
    def hdf_writefile_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDF_WriteFile_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDF_WriteFile_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_writefile_rbv)
    
    def hdf_writemessage(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDF_WriteMessage`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDF_WriteMessage` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_writemessage)
    
    def hdf_writestatus(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.HDF_WriteStatus`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.HDF_WriteStatus` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_writestatus)
    
    def init_buffer(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.Init_Buffer`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.Init_Buffer` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.init_buffer)
    
    def led_off(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.LED_Off`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.LED_Off` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.led_off)
    
    def led_on(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.LED_On`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.LED_On` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.led_on)
    
    def led_sta(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.LED_Sta`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.LED_Sta` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.led_sta)
    
    def magick_autosave(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.MAGICK_AutoSave`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.MAGICK_AutoSave` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_autosave)
    
    def magick_capture(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.MAGICK_Capture`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.MAGICK_Capture` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_capture)
    
    def magick_capture_disv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.MAGICK_Capture_DISV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.MAGICK_Capture_DISV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_capture_disv)
    
    def magick_capture_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.MAGICK_Capture_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.MAGICK_Capture_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_capture_rbv)
    
    def magick_filename(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.MAGICK_FileName`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.MAGICK_FileName` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_filename)
    
    def magick_filename_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.MAGICK_FileName_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.MAGICK_FileName_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_filename_rbv)
    
    def magick_filenumber(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.MAGICK_FileNumber`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.MAGICK_FileNumber` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_filenumber)
    
    def magick_filenumber_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.MAGICK_FileNumber_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.MAGICK_FileNumber_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_filenumber_rbv)
    
    def magick_filepath(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.MAGICK_FilePath`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.MAGICK_FilePath` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_filepath)
    
    def magick_filepath_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.MAGICK_FilePath_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.MAGICK_FilePath_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_filepath_rbv)
    
    def magick_filewritemode(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.MAGICK_FileWriteMode`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.MAGICK_FileWriteMode` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_filewritemode)
    
    def magick_numcapture(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.MAGICK_NumCapture`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.MAGICK_NumCapture` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_numcapture)
    
    def magick_numcapture_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.MAGICK_NumCapture_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.MAGICK_NumCapture_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_numcapture_rbv)
    
    def magick_writefile(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.MAGICK_WriteFile`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.MAGICK_WriteFile` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_writefile)
    
    def magick_writefile_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.MAGICK_WriteFile_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.MAGICK_WriteFile_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_writefile_rbv)
    
    def magick_writemessage(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.MAGICK_WriteMessage`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.MAGICK_WriteMessage` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_writemessage)
    
    def magick_writestatus(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.MAGICK_WriteStatus`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.MAGICK_WriteStatus` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_writestatus)
    
    def roi1_imagedata_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ROI1_ImageData_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ROI1_ImageData_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roi1_imagedata_rbv)
    
    def roi1_minx(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ROI1_MinX`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ROI1_MinX` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roi1_minx)
    
    def roi1_minx_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ROI1_MinX_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ROI1_MinX_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roi1_minx_rbv)
    
    def roi1_miny(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ROI1_MinY`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ROI1_MinY` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roi1_miny)
    
    def roi1_miny_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ROI1_MinY_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ROI1_MinY_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roi1_miny_rbv)
    
    def roi1_sizex(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ROI1_SizeX`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ROI1_SizeX` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roi1_sizex)
    
    def roi1_sizex_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ROI1_SizeX_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ROI1_SizeX_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roi1_sizex_rbv)
    
    def roi1_sizey(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ROI1_SizeY`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ROI1_SizeY` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roi1_sizey)
    
    def roi1_sizey_rbv(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ROI1_SizeY_RBV`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ROI1_SizeY_RBV` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roi1_sizey_rbv)
    
    def roiandmask_setx(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ROIandMask_SetX`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ROIandMask_SetX` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roiandmask_setx)
    
    def roiandmask_setxrad(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ROIandMask_SetXrad`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ROIandMask_SetXrad` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roiandmask_setxrad)
    
    def roiandmask_sety(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ROIandMask_SetY`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ROIandMask_SetY` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roiandmask_sety)
    
    def roiandmask_setyrad(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.ROIandMask_SetYrad`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.ROIandMask_SetYrad` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roiandmask_setyrad)
    
    def reset_buffer(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.Reset_Buffer`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.Reset_Buffer` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.reset_buffer)
    
    def save(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.Save`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.Save` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.save)
    
    def save_buffer(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.Save_Buffer`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.Save_Buffer` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.save_buffer)
    
    def save_buffer_path_initialise(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.Save_Buffer_Path_Initialise`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.Save_Buffer_Path_Initialise` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.save_buffer_path_initialise)
    
    def save_path_initialise(self, name: Union[str, List[str], None] = None):
        """
        Default Getter implementation for single, multiple, all values of: :attr:`CameraModel.Save_Path_Initialise`.

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the :attr:`CameraModel.Save_Path_Initialise` property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.save_path_initialise)
    