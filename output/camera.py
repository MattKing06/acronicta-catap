
from CATAP.common.machine.pv_utils import StatisticalPV, BinaryPV, ScalarPV, WaveformPV, StringPV, StatePV, PV
from CATAP.common.machine.hardware import PVMap, ControlsInformation, Properties, Hardware
from CATAP.common.machine.factory import Factory
from CATAP.common.machine.area import MachineArea
from typing import Any, Union, List, Dict
from pydantic import field_validator, SerializeAsAny, ConfigDict



class CameraPVMap(PVMap):
    
    ANA_AvgIntensity_RBV: StatisticalPV
    
    ANA_CPU_CropSubMask_RBV: StatisticalPV
    
    ANA_CPU_Dot_RBV: StatisticalPV
    
    ANA_CPU_Npoint_RBV: StatisticalPV
    
    ANA_CPU_RBV: StatisticalPV
    
    ANA_CenterX: StatisticalPV
    
    ANA_CenterX_RBV: StatisticalPV
    
    ANA_CenterY: StatisticalPV
    
    ANA_CenterY_RBV: StatisticalPV
    
    ANA_CovXYPix_RBV: StatisticalPV
    
    ANA_CovXY_RBV: StatisticalPV
    
    ANA_EnableCallbacks: BinaryPV
    
    ANA_EnableCallbacks_RBV: BinaryPV
    
    ANA_FloorLevel: ScalarPV
    
    ANA_FloorLevel_RBV: ScalarPV
    
    ANA_FlooredPercent_RBV: ScalarPV
    
    ANA_FlooredPoints_RBV: ScalarPV
    
    ANA_Intensity_RBV: StatisticalPV
    
    ANA_MMResults_RBV: WaveformPV
    
    ANA_MaskHeight_RBV: ScalarPV
    
    ANA_MaskWidth_RBV: ScalarPV
    
    ANA_MaskXCenter: ScalarPV
    
    ANA_MaskXCenter_RBV: ScalarPV
    
    ANA_MaskXRad: ScalarPV
    
    ANA_MaskXRad_RBV: ScalarPV
    
    ANA_MaskYCenter: ScalarPV
    
    ANA_MaskYCenter_RBV: ScalarPV
    
    ANA_MaskYRad: ScalarPV
    
    ANA_MaskYRad_RBV: ScalarPV
    
    ANA_NPointStepSize: ScalarPV
    
    ANA_NPointStepSize_RBV: ScalarPV
    
    ANA_NewBkgrnd: ScalarPV
    
    ANA_NewBkgrnd_RBV: ScalarPV
    
    ANA_OVERLAY_1_CROSS: BinaryPV
    
    ANA_OVERLAY_1_CROSS_RBV: BinaryPV
    
    ANA_OVERLAY_2_RESULT: BinaryPV
    
    ANA_OVERLAY_2_RESULT_RBV: BinaryPV
    
    ANA_OVERLAY_3_MASK: BinaryPV
    
    ANA_OVERLAY_3_MASK_RBV: BinaryPV
    
    ANA_PixH_RBV: ScalarPV
    
    ANA_PixMM: ScalarPV
    
    ANA_PixMM_RBV: ScalarPV
    
    ANA_PixW_RBV: ScalarPV
    
    ANA_PixelResults_RBV: WaveformPV
    
    ANA_SigmaXPix_RBV: StatisticalPV
    
    ANA_SigmaX_RBV: StatisticalPV
    
    ANA_SigmaYPix_RBV: StatisticalPV
    
    ANA_SigmaY_RBV: StatisticalPV
    
    ANA_UseBkgrnd: ScalarPV
    
    ANA_UseBkgrnd_RBV: ScalarPV
    
    ANA_UseFloor: ScalarPV
    
    ANA_UseFloor_RBV: ScalarPV
    
    ANA_UseNPoint: ScalarPV
    
    ANA_UseNPoint_RBV: ScalarPV
    
    ANA_XPix_RBV: StatisticalPV
    
    ANA_X_RBV: StatisticalPV
    
    ANA_YPix_RBV: StatisticalPV
    
    ANA_Y_RBV: StatisticalPV
    
    Buffer_Status: StringPV
    
    CAM1_ArrayData: WaveformPV
    
    CAM2_ArrayData: WaveformPV
    
    CAM_AcquirePeriod_RBV: ScalarPV
    
    CAM_AcquireTime_RBV: StatisticalPV
    
    CAM_Acquire_RBV: BinaryPV
    
    CAM_Active_Count: ScalarPV
    
    CAM_Active_Limit: ScalarPV
    
    CAM_ArrayRate_RBV: StatisticalPV
    
    CAM_Start_Acquire: BinaryPV
    
    CAM_Stop_Acquire: BinaryPV
    
    CAM_Temperature_RBV: ScalarPV
    
    HDFB_AutoSave: BinaryPV
    
    HDFB_Buffer_FileNumber: ScalarPV
    
    HDFB_Buffer_FileNumber_RBV: ScalarPV
    
    HDFB_Capture: BinaryPV
    
    HDFB_Capture_DISV: BinaryPV
    
    HDFB_Capture_RBV: BinaryPV
    
    HDFB_FileName: StringPV
    
    HDFB_FileName_RBV: StringPV
    
    HDFB_FileNumber: ScalarPV
    
    HDFB_FileNumber_RBV: StatisticalPV
    
    HDFB_FilePath: StringPV
    
    HDFB_FilePath_RBV: StringPV
    
    HDFB_FileWriteMode: StatePV
    
    HDFB_NumCapture: ScalarPV
    
    HDFB_NumCapture_RBV: ScalarPV
    
    HDFB_NumCaptured_RBV: ScalarPV
    
    HDFB_NumImagesCached_RBV: ScalarPV
    
    HDFB_PostCount: ScalarPV
    
    HDFB_PreCount: ScalarPV
    
    HDFB_WriteFile: BinaryPV
    
    HDFB_WriteFile_RBV: BinaryPV
    
    HDFB_WriteMessage: StringPV
    
    HDFB_WriteStatus: BinaryPV
    
    HDFB_image_buffer_fileName: StringPV
    
    HDFB_image_buffer_fileName_RBV: StringPV
    
    HDFB_image_buffer_filePath: StringPV
    
    HDFB_image_buffer_filePath_RBV: StringPV
    
    HDFB_image_buffer_trigger: ScalarPV
    
    HDFM_AutoSave: BinaryPV
    
    HDFM_Capture: BinaryPV
    
    HDFM_Capture_DISV: BinaryPV
    
    HDFM_Capture_RBV: BinaryPV
    
    HDFM_FileName: StringPV
    
    HDFM_FileName_RBV: StringPV
    
    HDFM_FileNumber: ScalarPV
    
    HDFM_FileNumber_RBV: StatisticalPV
    
    HDFM_FilePath: StringPV
    
    HDFM_FilePath_RBV: StringPV
    
    HDFM_FileWriteMode: StatePV
    
    HDFM_NumCapture: ScalarPV
    
    HDFM_NumCapture_RBV: ScalarPV
    
    HDFM_WriteFile: BinaryPV
    
    HDFM_WriteFile_RBV: BinaryPV
    
    HDFM_WriteMessage: StringPV
    
    HDFM_WriteStatus: BinaryPV
    
    HDF_AutoSave: BinaryPV
    
    HDF_Capture: BinaryPV
    
    HDF_Capture_DISV: BinaryPV
    
    HDF_Capture_RBV: BinaryPV
    
    HDF_FileName: StringPV
    
    HDF_FileName_RBV: StringPV
    
    HDF_FileNumber: ScalarPV
    
    HDF_FileNumber_RBV: StatisticalPV
    
    HDF_FilePath: StringPV
    
    HDF_FilePath_RBV: StringPV
    
    HDF_FileWriteMode: StatePV
    
    HDF_NumCapture: ScalarPV
    
    HDF_NumCapture_RBV: ScalarPV
    
    HDF_WriteFile: BinaryPV
    
    HDF_WriteFile_RBV: BinaryPV
    
    HDF_WriteMessage: StringPV
    
    HDF_WriteStatus: BinaryPV
    
    Init_Buffer: BinaryPV
    
    LED_Off: BinaryPV
    
    LED_On: BinaryPV
    
    LED_Sta: BinaryPV
    
    MAGICK_AutoSave: BinaryPV
    
    MAGICK_Capture: BinaryPV
    
    MAGICK_Capture_DISV: BinaryPV
    
    MAGICK_Capture_RBV: BinaryPV
    
    MAGICK_FileName: StringPV
    
    MAGICK_FileName_RBV: StringPV
    
    MAGICK_FileNumber: ScalarPV
    
    MAGICK_FileNumber_RBV: StatisticalPV
    
    MAGICK_FilePath: StringPV
    
    MAGICK_FilePath_RBV: StringPV
    
    MAGICK_FileWriteMode: StatePV
    
    MAGICK_NumCapture: ScalarPV
    
    MAGICK_NumCapture_RBV: ScalarPV
    
    MAGICK_WriteFile: BinaryPV
    
    MAGICK_WriteFile_RBV: BinaryPV
    
    MAGICK_WriteMessage: StringPV
    
    MAGICK_WriteStatus: BinaryPV
    
    ROI1_ImageData_RBV: WaveformPV
    
    ROI1_MinX: PV
    
    ROI1_MinX_RBV: PV
    
    ROI1_MinY: PV
    
    ROI1_MinY_RBV: PV
    
    ROI1_SizeX: PV
    
    ROI1_SizeX_RBV: PV
    
    ROI1_SizeY: PV
    
    ROI1_SizeY_RBV: PV
    
    ROIandMask_SetX: PV
    
    ROIandMask_SetXrad: PV
    
    ROIandMask_SetY: PV
    
    ROIandMask_SetYrad: PV
    
    Reset_Buffer: BinaryPV
    
    Save: BinaryPV
    
    Save_Buffer: BinaryPV
    
    Save_Buffer_Path_Initialise: BinaryPV
    
    Save_Path_Initialise: BinaryPV
    

    def __init__(
        self,
        is_virtual: bool,
        connect_on_creation: bool = False,
        *args,
        **kwargs,
    ):
        CameraPVMap.is_virtual = is_virtual
        CameraPVMap.connect_on_creation = connect_on_creation
        super(
            CameraPVMap,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    
    @property
    def ana_avgintensity_rbv(self):
        return self.ANA_AvgIntensity_RBV.get()
    
    
    @property
    def ana_cpu_cropsubmask_rbv(self):
        return self.ANA_CPU_CropSubMask_RBV.get()
    
    
    @property
    def ana_cpu_dot_rbv(self):
        return self.ANA_CPU_Dot_RBV.get()
    
    
    @property
    def ana_cpu_npoint_rbv(self):
        return self.ANA_CPU_Npoint_RBV.get()
    
    
    @property
    def ana_cpu_rbv(self):
        return self.ANA_CPU_RBV.get()
    
    
    @property
    def ana_centerx(self):
        return self.ANA_CenterX.get()
    
    
    @property
    def ana_centerx_rbv(self):
        return self.ANA_CenterX_RBV.get()
    
    
    @property
    def ana_centery(self):
        return self.ANA_CenterY.get()
    
    
    @property
    def ana_centery_rbv(self):
        return self.ANA_CenterY_RBV.get()
    
    
    @property
    def ana_covxypix_rbv(self):
        return self.ANA_CovXYPix_RBV.get()
    
    
    @property
    def ana_covxy_rbv(self):
        return self.ANA_CovXY_RBV.get()
    
    
    @property
    def ana_enablecallbacks(self):
        return self.ANA_EnableCallbacks.get()
    
    @ana_enablecallbacks.setter
    def ana_enablecallbacks(self, value):
        self.ANA_EnableCallbacks.put(value)
    
    
    @property
    def ana_enablecallbacks_rbv(self):
        return self.ANA_EnableCallbacks_RBV.get()
    
    
    @property
    def ana_floorlevel(self):
        return self.ANA_FloorLevel.get()
    
    
    @property
    def ana_floorlevel_rbv(self):
        return self.ANA_FloorLevel_RBV.get()
    
    
    @property
    def ana_flooredpercent_rbv(self):
        return self.ANA_FlooredPercent_RBV.get()
    
    
    @property
    def ana_flooredpoints_rbv(self):
        return self.ANA_FlooredPoints_RBV.get()
    
    
    @property
    def ana_intensity_rbv(self):
        return self.ANA_Intensity_RBV.get()
    
    
    @property
    def ana_mmresults_rbv(self):
        return self.ANA_MMResults_RBV.get()
    
    
    @property
    def ana_maskheight_rbv(self):
        return self.ANA_MaskHeight_RBV.get()
    
    
    @property
    def ana_maskwidth_rbv(self):
        return self.ANA_MaskWidth_RBV.get()
    
    
    @property
    def ana_maskxcenter(self):
        return self.ANA_MaskXCenter.get()
    
    
    @property
    def ana_maskxcenter_rbv(self):
        return self.ANA_MaskXCenter_RBV.get()
    
    
    @property
    def ana_maskxrad(self):
        return self.ANA_MaskXRad.get()
    
    
    @property
    def ana_maskxrad_rbv(self):
        return self.ANA_MaskXRad_RBV.get()
    
    
    @property
    def ana_maskycenter(self):
        return self.ANA_MaskYCenter.get()
    
    
    @property
    def ana_maskycenter_rbv(self):
        return self.ANA_MaskYCenter_RBV.get()
    
    
    @property
    def ana_maskyrad(self):
        return self.ANA_MaskYRad.get()
    
    
    @property
    def ana_maskyrad_rbv(self):
        return self.ANA_MaskYRad_RBV.get()
    
    
    @property
    def ana_npointstepsize(self):
        return self.ANA_NPointStepSize.get()
    
    
    @property
    def ana_npointstepsize_rbv(self):
        return self.ANA_NPointStepSize_RBV.get()
    
    
    @property
    def ana_newbkgrnd(self):
        return self.ANA_NewBkgrnd.get()
    
    
    @property
    def ana_newbkgrnd_rbv(self):
        return self.ANA_NewBkgrnd_RBV.get()
    
    
    @property
    def ana_overlay_1_cross(self):
        return self.ANA_OVERLAY_1_CROSS.get()
    
    
    @property
    def ana_overlay_1_cross_rbv(self):
        return self.ANA_OVERLAY_1_CROSS_RBV.get()
    
    
    @property
    def ana_overlay_2_result(self):
        return self.ANA_OVERLAY_2_RESULT.get()
    
    
    @property
    def ana_overlay_2_result_rbv(self):
        return self.ANA_OVERLAY_2_RESULT_RBV.get()
    
    
    @property
    def ana_overlay_3_mask(self):
        return self.ANA_OVERLAY_3_MASK.get()
    
    
    @property
    def ana_overlay_3_mask_rbv(self):
        return self.ANA_OVERLAY_3_MASK_RBV.get()
    
    
    @property
    def ana_pixh_rbv(self):
        return self.ANA_PixH_RBV.get()
    
    
    @property
    def ana_pixmm(self):
        return self.ANA_PixMM.get()
    
    
    @property
    def ana_pixmm_rbv(self):
        return self.ANA_PixMM_RBV.get()
    
    
    @property
    def ana_pixw_rbv(self):
        return self.ANA_PixW_RBV.get()
    
    
    @property
    def ana_pixelresults_rbv(self):
        return self.ANA_PixelResults_RBV.get()
    
    
    @property
    def ana_sigmaxpix_rbv(self):
        return self.ANA_SigmaXPix_RBV.get()
    
    
    @property
    def ana_sigmax_rbv(self):
        return self.ANA_SigmaX_RBV.get()
    
    
    @property
    def ana_sigmaypix_rbv(self):
        return self.ANA_SigmaYPix_RBV.get()
    
    
    @property
    def ana_sigmay_rbv(self):
        return self.ANA_SigmaY_RBV.get()
    
    
    @property
    def ana_usebkgrnd(self):
        return self.ANA_UseBkgrnd.get()
    
    
    @property
    def ana_usebkgrnd_rbv(self):
        return self.ANA_UseBkgrnd_RBV.get()
    
    
    @property
    def ana_usefloor(self):
        return self.ANA_UseFloor.get()
    
    
    @property
    def ana_usefloor_rbv(self):
        return self.ANA_UseFloor_RBV.get()
    
    
    @property
    def ana_usenpoint(self):
        return self.ANA_UseNPoint.get()
    
    
    @property
    def ana_usenpoint_rbv(self):
        return self.ANA_UseNPoint_RBV.get()
    
    
    @property
    def ana_xpix_rbv(self):
        return self.ANA_XPix_RBV.get()
    
    
    @property
    def ana_x_rbv(self):
        return self.ANA_X_RBV.get()
    
    
    @property
    def ana_ypix_rbv(self):
        return self.ANA_YPix_RBV.get()
    
    
    @property
    def ana_y_rbv(self):
        return self.ANA_Y_RBV.get()
    
    
    @property
    def buffer_status(self):
        return self.Buffer_Status.get()
    
    
    @property
    def cam1_arraydata(self):
        return self.CAM1_ArrayData.get()
    
    
    @property
    def cam2_arraydata(self):
        return self.CAM2_ArrayData.get()
    
    
    @property
    def cam_acquireperiod_rbv(self):
        return self.CAM_AcquirePeriod_RBV.get()
    
    
    @property
    def cam_acquiretime_rbv(self):
        return self.CAM_AcquireTime_RBV.get()
    
    
    @property
    def cam_acquire_rbv(self):
        return self.CAM_Acquire_RBV.get()
    
    
    @property
    def cam_active_count(self):
        return self.CAM_Active_Count.get()
    
    
    @property
    def cam_active_limit(self):
        return self.CAM_Active_Limit.get()
    
    
    @property
    def cam_arrayrate_rbv(self):
        return self.CAM_ArrayRate_RBV.get()
    
    
    @property
    def cam_start_acquire(self):
        return self.CAM_Start_Acquire.get()
    
    @cam_start_acquire.setter
    def cam_start_acquire(self, value):
        self.CAM_Start_Acquire.put(value)
    
    
    @property
    def cam_stop_acquire(self):
        return self.CAM_Stop_Acquire.get()
    
    @cam_stop_acquire.setter
    def cam_stop_acquire(self, value):
        self.CAM_Stop_Acquire.put(value)
    
    
    @property
    def cam_temperature_rbv(self):
        return self.CAM_Temperature_RBV.get()
    
    
    @property
    def hdfb_autosave(self):
        return self.HDFB_AutoSave.get()
    
    @hdfb_autosave.setter
    def hdfb_autosave(self, value):
        self.HDFB_AutoSave.put(value)
    
    
    @property
    def hdfb_buffer_filenumber(self):
        return self.HDFB_Buffer_FileNumber.get()
    
    
    @property
    def hdfb_buffer_filenumber_rbv(self):
        return self.HDFB_Buffer_FileNumber_RBV.get()
    
    
    @property
    def hdfb_capture(self):
        return self.HDFB_Capture.get()
    
    @hdfb_capture.setter
    def hdfb_capture(self, value):
        self.HDFB_Capture.put(value)
    
    
    @property
    def hdfb_capture_disv(self):
        return self.HDFB_Capture_DISV.get()
    
    @hdfb_capture_disv.setter
    def hdfb_capture_disv(self, value):
        self.HDFB_Capture_DISV.put(value)
    
    
    @property
    def hdfb_capture_rbv(self):
        return self.HDFB_Capture_RBV.get()
    
    
    @property
    def hdfb_filename(self):
        return self.HDFB_FileName.get()
    
    
    @property
    def hdfb_filename_rbv(self):
        return self.HDFB_FileName_RBV.get()
    
    
    @property
    def hdfb_filenumber(self):
        return self.HDFB_FileNumber.get()
    
    
    @property
    def hdfb_filenumber_rbv(self):
        return self.HDFB_FileNumber_RBV.get()
    
    
    @property
    def hdfb_filepath(self):
        return self.HDFB_FilePath.get()
    
    
    @property
    def hdfb_filepath_rbv(self):
        return self.HDFB_FilePath_RBV.get()
    
    
    @property
    def hdfb_filewritemode(self):
        return self.HDFB_FileWriteMode.get()
    
    @hdfb_filewritemode.setter
    def hdfb_filewritemode(self, value):
        self.HDFB_FileWriteMode.put(value)
    
    
    @property
    def hdfb_numcapture(self):
        return self.HDFB_NumCapture.get()
    
    @hdfb_numcapture.setter
    def hdfb_numcapture(self, value):
        self.HDFB_NumCapture.put(value)
    
    
    @property
    def hdfb_numcapture_rbv(self):
        return self.HDFB_NumCapture_RBV.get()
    
    
    @property
    def hdfb_numcaptured_rbv(self):
        return self.HDFB_NumCaptured_RBV.get()
    
    
    @property
    def hdfb_numimagescached_rbv(self):
        return self.HDFB_NumImagesCached_RBV.get()
    
    
    @property
    def hdfb_postcount(self):
        return self.HDFB_PostCount.get()
    
    @hdfb_postcount.setter
    def hdfb_postcount(self, value):
        self.HDFB_PostCount.put(value)
    
    
    @property
    def hdfb_precount(self):
        return self.HDFB_PreCount.get()
    
    @hdfb_precount.setter
    def hdfb_precount(self, value):
        self.HDFB_PreCount.put(value)
    
    
    @property
    def hdfb_writefile(self):
        return self.HDFB_WriteFile.get()
    
    
    @property
    def hdfb_writefile_rbv(self):
        return self.HDFB_WriteFile_RBV.get()
    
    
    @property
    def hdfb_writemessage(self):
        return self.HDFB_WriteMessage.get()
    
    
    @property
    def hdfb_writestatus(self):
        return self.HDFB_WriteStatus.get()
    
    
    @property
    def hdfb_image_buffer_filename(self):
        return self.HDFB_image_buffer_fileName.get()
    
    
    @property
    def hdfb_image_buffer_filename_rbv(self):
        return self.HDFB_image_buffer_fileName_RBV.get()
    
    
    @property
    def hdfb_image_buffer_filepath(self):
        return self.HDFB_image_buffer_filePath.get()
    
    
    @property
    def hdfb_image_buffer_filepath_rbv(self):
        return self.HDFB_image_buffer_filePath_RBV.get()
    
    
    @property
    def hdfb_image_buffer_trigger(self):
        return self.HDFB_image_buffer_trigger.get()
    
    
    @property
    def hdfm_autosave(self):
        return self.HDFM_AutoSave.get()
    
    @hdfm_autosave.setter
    def hdfm_autosave(self, value):
        self.HDFM_AutoSave.put(value)
    
    
    @property
    def hdfm_capture(self):
        return self.HDFM_Capture.get()
    
    @hdfm_capture.setter
    def hdfm_capture(self, value):
        self.HDFM_Capture.put(value)
    
    
    @property
    def hdfm_capture_disv(self):
        return self.HDFM_Capture_DISV.get()
    
    @hdfm_capture_disv.setter
    def hdfm_capture_disv(self, value):
        self.HDFM_Capture_DISV.put(value)
    
    
    @property
    def hdfm_capture_rbv(self):
        return self.HDFM_Capture_RBV.get()
    
    
    @property
    def hdfm_filename(self):
        return self.HDFM_FileName.get()
    
    
    @property
    def hdfm_filename_rbv(self):
        return self.HDFM_FileName_RBV.get()
    
    
    @property
    def hdfm_filenumber(self):
        return self.HDFM_FileNumber.get()
    
    
    @property
    def hdfm_filenumber_rbv(self):
        return self.HDFM_FileNumber_RBV.get()
    
    
    @property
    def hdfm_filepath(self):
        return self.HDFM_FilePath.get()
    
    
    @property
    def hdfm_filepath_rbv(self):
        return self.HDFM_FilePath_RBV.get()
    
    
    @property
    def hdfm_filewritemode(self):
        return self.HDFM_FileWriteMode.get()
    
    @hdfm_filewritemode.setter
    def hdfm_filewritemode(self, value):
        self.HDFM_FileWriteMode.put(value)
    
    
    @property
    def hdfm_numcapture(self):
        return self.HDFM_NumCapture.get()
    
    @hdfm_numcapture.setter
    def hdfm_numcapture(self, value):
        self.HDFM_NumCapture.put(value)
    
    
    @property
    def hdfm_numcapture_rbv(self):
        return self.HDFM_NumCapture_RBV.get()
    
    
    @property
    def hdfm_writefile(self):
        return self.HDFM_WriteFile.get()
    
    
    @property
    def hdfm_writefile_rbv(self):
        return self.HDFM_WriteFile_RBV.get()
    
    
    @property
    def hdfm_writemessage(self):
        return self.HDFM_WriteMessage.get()
    
    
    @property
    def hdfm_writestatus(self):
        return self.HDFM_WriteStatus.get()
    
    
    @property
    def hdf_autosave(self):
        return self.HDF_AutoSave.get()
    
    @hdf_autosave.setter
    def hdf_autosave(self, value):
        self.HDF_AutoSave.put(value)
    
    
    @property
    def hdf_capture(self):
        return self.HDF_Capture.get()
    
    @hdf_capture.setter
    def hdf_capture(self, value):
        self.HDF_Capture.put(value)
    
    
    @property
    def hdf_capture_disv(self):
        return self.HDF_Capture_DISV.get()
    
    @hdf_capture_disv.setter
    def hdf_capture_disv(self, value):
        self.HDF_Capture_DISV.put(value)
    
    
    @property
    def hdf_capture_rbv(self):
        return self.HDF_Capture_RBV.get()
    
    
    @property
    def hdf_filename(self):
        return self.HDF_FileName.get()
    
    
    @property
    def hdf_filename_rbv(self):
        return self.HDF_FileName_RBV.get()
    
    
    @property
    def hdf_filenumber(self):
        return self.HDF_FileNumber.get()
    
    
    @property
    def hdf_filenumber_rbv(self):
        return self.HDF_FileNumber_RBV.get()
    
    
    @property
    def hdf_filepath(self):
        return self.HDF_FilePath.get()
    
    
    @property
    def hdf_filepath_rbv(self):
        return self.HDF_FilePath_RBV.get()
    
    
    @property
    def hdf_filewritemode(self):
        return self.HDF_FileWriteMode.get()
    
    @hdf_filewritemode.setter
    def hdf_filewritemode(self, value):
        self.HDF_FileWriteMode.put(value)
    
    
    @property
    def hdf_numcapture(self):
        return self.HDF_NumCapture.get()
    
    @hdf_numcapture.setter
    def hdf_numcapture(self, value):
        self.HDF_NumCapture.put(value)
    
    
    @property
    def hdf_numcapture_rbv(self):
        return self.HDF_NumCapture_RBV.get()
    
    
    @property
    def hdf_writefile(self):
        return self.HDF_WriteFile.get()
    
    
    @property
    def hdf_writefile_rbv(self):
        return self.HDF_WriteFile_RBV.get()
    
    
    @property
    def hdf_writemessage(self):
        return self.HDF_WriteMessage.get()
    
    
    @property
    def hdf_writestatus(self):
        return self.HDF_WriteStatus.get()
    
    
    @property
    def init_buffer(self):
        return self.Init_Buffer.get()
    
    @init_buffer.setter
    def init_buffer(self, value):
        self.Init_Buffer.put(value)
    
    
    @property
    def led_off(self):
        return self.LED_Off.get()
    
    @led_off.setter
    def led_off(self, value):
        self.LED_Off.put(value)
    
    
    @property
    def led_on(self):
        return self.LED_On.get()
    
    @led_on.setter
    def led_on(self, value):
        self.LED_On.put(value)
    
    
    @property
    def led_sta(self):
        return self.LED_Sta.get()
    
    
    @property
    def magick_autosave(self):
        return self.MAGICK_AutoSave.get()
    
    @magick_autosave.setter
    def magick_autosave(self, value):
        self.MAGICK_AutoSave.put(value)
    
    
    @property
    def magick_capture(self):
        return self.MAGICK_Capture.get()
    
    @magick_capture.setter
    def magick_capture(self, value):
        self.MAGICK_Capture.put(value)
    
    
    @property
    def magick_capture_disv(self):
        return self.MAGICK_Capture_DISV.get()
    
    @magick_capture_disv.setter
    def magick_capture_disv(self, value):
        self.MAGICK_Capture_DISV.put(value)
    
    
    @property
    def magick_capture_rbv(self):
        return self.MAGICK_Capture_RBV.get()
    
    
    @property
    def magick_filename(self):
        return self.MAGICK_FileName.get()
    
    
    @property
    def magick_filename_rbv(self):
        return self.MAGICK_FileName_RBV.get()
    
    
    @property
    def magick_filenumber(self):
        return self.MAGICK_FileNumber.get()
    
    
    @property
    def magick_filenumber_rbv(self):
        return self.MAGICK_FileNumber_RBV.get()
    
    
    @property
    def magick_filepath(self):
        return self.MAGICK_FilePath.get()
    
    
    @property
    def magick_filepath_rbv(self):
        return self.MAGICK_FilePath_RBV.get()
    
    
    @property
    def magick_filewritemode(self):
        return self.MAGICK_FileWriteMode.get()
    
    @magick_filewritemode.setter
    def magick_filewritemode(self, value):
        self.MAGICK_FileWriteMode.put(value)
    
    
    @property
    def magick_numcapture(self):
        return self.MAGICK_NumCapture.get()
    
    @magick_numcapture.setter
    def magick_numcapture(self, value):
        self.MAGICK_NumCapture.put(value)
    
    
    @property
    def magick_numcapture_rbv(self):
        return self.MAGICK_NumCapture_RBV.get()
    
    
    @property
    def magick_writefile(self):
        return self.MAGICK_WriteFile.get()
    
    
    @property
    def magick_writefile_rbv(self):
        return self.MAGICK_WriteFile_RBV.get()
    
    
    @property
    def magick_writemessage(self):
        return self.MAGICK_WriteMessage.get()
    
    
    @property
    def magick_writestatus(self):
        return self.MAGICK_WriteStatus.get()
    
    
    @property
    def roi1_imagedata_rbv(self):
        return self.ROI1_ImageData_RBV.get()
    
    
    @property
    def roi1_minx(self):
        return self.ROI1_MinX.get()
    
    
    @property
    def roi1_minx_rbv(self):
        return self.ROI1_MinX_RBV.get()
    
    
    @property
    def roi1_miny(self):
        return self.ROI1_MinY.get()
    
    
    @property
    def roi1_miny_rbv(self):
        return self.ROI1_MinY_RBV.get()
    
    
    @property
    def roi1_sizex(self):
        return self.ROI1_SizeX.get()
    
    
    @property
    def roi1_sizex_rbv(self):
        return self.ROI1_SizeX_RBV.get()
    
    
    @property
    def roi1_sizey(self):
        return self.ROI1_SizeY.get()
    
    
    @property
    def roi1_sizey_rbv(self):
        return self.ROI1_SizeY_RBV.get()
    
    
    @property
    def roiandmask_setx(self):
        return self.ROIandMask_SetX.get()
    
    
    @property
    def roiandmask_setxrad(self):
        return self.ROIandMask_SetXrad.get()
    
    
    @property
    def roiandmask_sety(self):
        return self.ROIandMask_SetY.get()
    
    
    @property
    def roiandmask_setyrad(self):
        return self.ROIandMask_SetYrad.get()
    
    
    @property
    def reset_buffer(self):
        return self.Reset_Buffer.get()
    
    @reset_buffer.setter
    def reset_buffer(self, value):
        self.Reset_Buffer.put(value)
    
    
    @property
    def save(self):
        return self.Save.get()
    
    @save.setter
    def save(self, value):
        self.Save.put(value)
    
    
    @property
    def save_buffer(self):
        return self.Save_Buffer.get()
    
    @save_buffer.setter
    def save_buffer(self, value):
        self.Save_Buffer.put(value)
    
    
    @property
    def save_buffer_path_initialise(self):
        return self.Save_Buffer_Path_Initialise.get()
    
    @save_buffer_path_initialise.setter
    def save_buffer_path_initialise(self, value):
        self.Save_Buffer_Path_Initialise.put(value)
    
    
    @property
    def save_path_initialise(self):
        return self.Save_Path_Initialise.get()
    
    @save_path_initialise.setter
    def save_path_initialise(self, value):
        self.Save_Path_Initialise.put(value)
    
    



class CameraControlsInformation(ControlsInformation):
    """
    Class for controlling a camera via EPICS

    Inherits from:
        :class:`~CATAP.common.machine.hardware.ControlsInformation`
    """
    pv_record_map: SerializeAsAny[CameraPVMap]
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
        CameraControlsInformation.is_virtual = is_virtual
        CameraControlsInformation.connect_on_creation = connect_on_creation
        super(
            CameraControlsInformation,
            self,
        ).__init__(
            is_virtual=is_virtual,
            connect_on_creation=connect_on_creation,
            *args,
            **kwargs,
        )

    @field_validator("pv_record_map", mode="before")
    @classmethod
    def validate_pv_map(cls, v: Any) -> CameraPVMap:
        return CameraPVMap(
            is_virtual=cls.is_virtual,
            connect_on_creation=cls.connect_on_creation,
            **v,
        )

    
    @property
    def ana_avgintensity_rbv(self):
        return self.pv_record_map.ana_avgintensity_rbv
    
    
    @property
    def ana_cpu_cropsubmask_rbv(self):
        return self.pv_record_map.ana_cpu_cropsubmask_rbv
    
    
    @property
    def ana_cpu_dot_rbv(self):
        return self.pv_record_map.ana_cpu_dot_rbv
    
    
    @property
    def ana_cpu_npoint_rbv(self):
        return self.pv_record_map.ana_cpu_npoint_rbv
    
    
    @property
    def ana_cpu_rbv(self):
        return self.pv_record_map.ana_cpu_rbv
    
    
    @property
    def ana_centerx(self):
        return self.pv_record_map.ana_centerx
    
    
    @property
    def ana_centerx_rbv(self):
        return self.pv_record_map.ana_centerx_rbv
    
    
    @property
    def ana_centery(self):
        return self.pv_record_map.ana_centery
    
    
    @property
    def ana_centery_rbv(self):
        return self.pv_record_map.ana_centery_rbv
    
    
    @property
    def ana_covxypix_rbv(self):
        return self.pv_record_map.ana_covxypix_rbv
    
    
    @property
    def ana_covxy_rbv(self):
        return self.pv_record_map.ana_covxy_rbv
    
    
    @property
    def ana_enablecallbacks(self):
        return self.pv_record_map.ana_enablecallbacks
    
    @ana_enablecallbacks.setter
    def ana_enablecallbacks(self, value):
        self.pv_record_map.ana_enablecallbacks = value
    
    
    @property
    def ana_enablecallbacks_rbv(self):
        return self.pv_record_map.ana_enablecallbacks_rbv
    
    
    @property
    def ana_floorlevel(self):
        return self.pv_record_map.ana_floorlevel
    
    
    @property
    def ana_floorlevel_rbv(self):
        return self.pv_record_map.ana_floorlevel_rbv
    
    
    @property
    def ana_flooredpercent_rbv(self):
        return self.pv_record_map.ana_flooredpercent_rbv
    
    
    @property
    def ana_flooredpoints_rbv(self):
        return self.pv_record_map.ana_flooredpoints_rbv
    
    
    @property
    def ana_intensity_rbv(self):
        return self.pv_record_map.ana_intensity_rbv
    
    
    @property
    def ana_mmresults_rbv(self):
        return self.pv_record_map.ana_mmresults_rbv
    
    
    @property
    def ana_maskheight_rbv(self):
        return self.pv_record_map.ana_maskheight_rbv
    
    
    @property
    def ana_maskwidth_rbv(self):
        return self.pv_record_map.ana_maskwidth_rbv
    
    
    @property
    def ana_maskxcenter(self):
        return self.pv_record_map.ana_maskxcenter
    
    
    @property
    def ana_maskxcenter_rbv(self):
        return self.pv_record_map.ana_maskxcenter_rbv
    
    
    @property
    def ana_maskxrad(self):
        return self.pv_record_map.ana_maskxrad
    
    
    @property
    def ana_maskxrad_rbv(self):
        return self.pv_record_map.ana_maskxrad_rbv
    
    
    @property
    def ana_maskycenter(self):
        return self.pv_record_map.ana_maskycenter
    
    
    @property
    def ana_maskycenter_rbv(self):
        return self.pv_record_map.ana_maskycenter_rbv
    
    
    @property
    def ana_maskyrad(self):
        return self.pv_record_map.ana_maskyrad
    
    
    @property
    def ana_maskyrad_rbv(self):
        return self.pv_record_map.ana_maskyrad_rbv
    
    
    @property
    def ana_npointstepsize(self):
        return self.pv_record_map.ana_npointstepsize
    
    
    @property
    def ana_npointstepsize_rbv(self):
        return self.pv_record_map.ana_npointstepsize_rbv
    
    
    @property
    def ana_newbkgrnd(self):
        return self.pv_record_map.ana_newbkgrnd
    
    
    @property
    def ana_newbkgrnd_rbv(self):
        return self.pv_record_map.ana_newbkgrnd_rbv
    
    
    @property
    def ana_overlay_1_cross(self):
        return self.pv_record_map.ana_overlay_1_cross
    
    
    @property
    def ana_overlay_1_cross_rbv(self):
        return self.pv_record_map.ana_overlay_1_cross_rbv
    
    
    @property
    def ana_overlay_2_result(self):
        return self.pv_record_map.ana_overlay_2_result
    
    
    @property
    def ana_overlay_2_result_rbv(self):
        return self.pv_record_map.ana_overlay_2_result_rbv
    
    
    @property
    def ana_overlay_3_mask(self):
        return self.pv_record_map.ana_overlay_3_mask
    
    
    @property
    def ana_overlay_3_mask_rbv(self):
        return self.pv_record_map.ana_overlay_3_mask_rbv
    
    
    @property
    def ana_pixh_rbv(self):
        return self.pv_record_map.ana_pixh_rbv
    
    
    @property
    def ana_pixmm(self):
        return self.pv_record_map.ana_pixmm
    
    
    @property
    def ana_pixmm_rbv(self):
        return self.pv_record_map.ana_pixmm_rbv
    
    
    @property
    def ana_pixw_rbv(self):
        return self.pv_record_map.ana_pixw_rbv
    
    
    @property
    def ana_pixelresults_rbv(self):
        return self.pv_record_map.ana_pixelresults_rbv
    
    
    @property
    def ana_sigmaxpix_rbv(self):
        return self.pv_record_map.ana_sigmaxpix_rbv
    
    
    @property
    def ana_sigmax_rbv(self):
        return self.pv_record_map.ana_sigmax_rbv
    
    
    @property
    def ana_sigmaypix_rbv(self):
        return self.pv_record_map.ana_sigmaypix_rbv
    
    
    @property
    def ana_sigmay_rbv(self):
        return self.pv_record_map.ana_sigmay_rbv
    
    
    @property
    def ana_usebkgrnd(self):
        return self.pv_record_map.ana_usebkgrnd
    
    
    @property
    def ana_usebkgrnd_rbv(self):
        return self.pv_record_map.ana_usebkgrnd_rbv
    
    
    @property
    def ana_usefloor(self):
        return self.pv_record_map.ana_usefloor
    
    
    @property
    def ana_usefloor_rbv(self):
        return self.pv_record_map.ana_usefloor_rbv
    
    
    @property
    def ana_usenpoint(self):
        return self.pv_record_map.ana_usenpoint
    
    
    @property
    def ana_usenpoint_rbv(self):
        return self.pv_record_map.ana_usenpoint_rbv
    
    
    @property
    def ana_xpix_rbv(self):
        return self.pv_record_map.ana_xpix_rbv
    
    
    @property
    def ana_x_rbv(self):
        return self.pv_record_map.ana_x_rbv
    
    
    @property
    def ana_ypix_rbv(self):
        return self.pv_record_map.ana_ypix_rbv
    
    
    @property
    def ana_y_rbv(self):
        return self.pv_record_map.ana_y_rbv
    
    
    @property
    def buffer_status(self):
        return self.pv_record_map.buffer_status
    
    
    @property
    def cam1_arraydata(self):
        return self.pv_record_map.cam1_arraydata
    
    
    @property
    def cam2_arraydata(self):
        return self.pv_record_map.cam2_arraydata
    
    
    @property
    def cam_acquireperiod_rbv(self):
        return self.pv_record_map.cam_acquireperiod_rbv
    
    
    @property
    def cam_acquiretime_rbv(self):
        return self.pv_record_map.cam_acquiretime_rbv
    
    
    @property
    def cam_acquire_rbv(self):
        return self.pv_record_map.cam_acquire_rbv
    
    
    @property
    def cam_active_count(self):
        return self.pv_record_map.cam_active_count
    
    
    @property
    def cam_active_limit(self):
        return self.pv_record_map.cam_active_limit
    
    
    @property
    def cam_arrayrate_rbv(self):
        return self.pv_record_map.cam_arrayrate_rbv
    
    
    @property
    def cam_start_acquire(self):
        return self.pv_record_map.cam_start_acquire
    
    @cam_start_acquire.setter
    def cam_start_acquire(self, value):
        self.pv_record_map.cam_start_acquire = value
    
    
    @property
    def cam_stop_acquire(self):
        return self.pv_record_map.cam_stop_acquire
    
    @cam_stop_acquire.setter
    def cam_stop_acquire(self, value):
        self.pv_record_map.cam_stop_acquire = value
    
    
    @property
    def cam_temperature_rbv(self):
        return self.pv_record_map.cam_temperature_rbv
    
    
    @property
    def hdfb_autosave(self):
        return self.pv_record_map.hdfb_autosave
    
    @hdfb_autosave.setter
    def hdfb_autosave(self, value):
        self.pv_record_map.hdfb_autosave = value
    
    
    @property
    def hdfb_buffer_filenumber(self):
        return self.pv_record_map.hdfb_buffer_filenumber
    
    
    @property
    def hdfb_buffer_filenumber_rbv(self):
        return self.pv_record_map.hdfb_buffer_filenumber_rbv
    
    
    @property
    def hdfb_capture(self):
        return self.pv_record_map.hdfb_capture
    
    @hdfb_capture.setter
    def hdfb_capture(self, value):
        self.pv_record_map.hdfb_capture = value
    
    
    @property
    def hdfb_capture_disv(self):
        return self.pv_record_map.hdfb_capture_disv
    
    @hdfb_capture_disv.setter
    def hdfb_capture_disv(self, value):
        self.pv_record_map.hdfb_capture_disv = value
    
    
    @property
    def hdfb_capture_rbv(self):
        return self.pv_record_map.hdfb_capture_rbv
    
    
    @property
    def hdfb_filename(self):
        return self.pv_record_map.hdfb_filename
    
    
    @property
    def hdfb_filename_rbv(self):
        return self.pv_record_map.hdfb_filename_rbv
    
    
    @property
    def hdfb_filenumber(self):
        return self.pv_record_map.hdfb_filenumber
    
    
    @property
    def hdfb_filenumber_rbv(self):
        return self.pv_record_map.hdfb_filenumber_rbv
    
    
    @property
    def hdfb_filepath(self):
        return self.pv_record_map.hdfb_filepath
    
    
    @property
    def hdfb_filepath_rbv(self):
        return self.pv_record_map.hdfb_filepath_rbv
    
    
    @property
    def hdfb_filewritemode(self):
        return self.pv_record_map.hdfb_filewritemode
    
    @hdfb_filewritemode.setter
    def hdfb_filewritemode(self, value):
        self.pv_record_map.hdfb_filewritemode = value
    
    
    @property
    def hdfb_numcapture(self):
        return self.pv_record_map.hdfb_numcapture
    
    @hdfb_numcapture.setter
    def hdfb_numcapture(self, value):
        self.pv_record_map.hdfb_numcapture = value
    
    
    @property
    def hdfb_numcapture_rbv(self):
        return self.pv_record_map.hdfb_numcapture_rbv
    
    
    @property
    def hdfb_numcaptured_rbv(self):
        return self.pv_record_map.hdfb_numcaptured_rbv
    
    
    @property
    def hdfb_numimagescached_rbv(self):
        return self.pv_record_map.hdfb_numimagescached_rbv
    
    
    @property
    def hdfb_postcount(self):
        return self.pv_record_map.hdfb_postcount
    
    @hdfb_postcount.setter
    def hdfb_postcount(self, value):
        self.pv_record_map.hdfb_postcount = value
    
    
    @property
    def hdfb_precount(self):
        return self.pv_record_map.hdfb_precount
    
    @hdfb_precount.setter
    def hdfb_precount(self, value):
        self.pv_record_map.hdfb_precount = value
    
    
    @property
    def hdfb_writefile(self):
        return self.pv_record_map.hdfb_writefile
    
    
    @property
    def hdfb_writefile_rbv(self):
        return self.pv_record_map.hdfb_writefile_rbv
    
    
    @property
    def hdfb_writemessage(self):
        return self.pv_record_map.hdfb_writemessage
    
    
    @property
    def hdfb_writestatus(self):
        return self.pv_record_map.hdfb_writestatus
    
    
    @property
    def hdfb_image_buffer_filename(self):
        return self.pv_record_map.hdfb_image_buffer_filename
    
    
    @property
    def hdfb_image_buffer_filename_rbv(self):
        return self.pv_record_map.hdfb_image_buffer_filename_rbv
    
    
    @property
    def hdfb_image_buffer_filepath(self):
        return self.pv_record_map.hdfb_image_buffer_filepath
    
    
    @property
    def hdfb_image_buffer_filepath_rbv(self):
        return self.pv_record_map.hdfb_image_buffer_filepath_rbv
    
    
    @property
    def hdfb_image_buffer_trigger(self):
        return self.pv_record_map.hdfb_image_buffer_trigger
    
    
    @property
    def hdfm_autosave(self):
        return self.pv_record_map.hdfm_autosave
    
    @hdfm_autosave.setter
    def hdfm_autosave(self, value):
        self.pv_record_map.hdfm_autosave = value
    
    
    @property
    def hdfm_capture(self):
        return self.pv_record_map.hdfm_capture
    
    @hdfm_capture.setter
    def hdfm_capture(self, value):
        self.pv_record_map.hdfm_capture = value
    
    
    @property
    def hdfm_capture_disv(self):
        return self.pv_record_map.hdfm_capture_disv
    
    @hdfm_capture_disv.setter
    def hdfm_capture_disv(self, value):
        self.pv_record_map.hdfm_capture_disv = value
    
    
    @property
    def hdfm_capture_rbv(self):
        return self.pv_record_map.hdfm_capture_rbv
    
    
    @property
    def hdfm_filename(self):
        return self.pv_record_map.hdfm_filename
    
    
    @property
    def hdfm_filename_rbv(self):
        return self.pv_record_map.hdfm_filename_rbv
    
    
    @property
    def hdfm_filenumber(self):
        return self.pv_record_map.hdfm_filenumber
    
    
    @property
    def hdfm_filenumber_rbv(self):
        return self.pv_record_map.hdfm_filenumber_rbv
    
    
    @property
    def hdfm_filepath(self):
        return self.pv_record_map.hdfm_filepath
    
    
    @property
    def hdfm_filepath_rbv(self):
        return self.pv_record_map.hdfm_filepath_rbv
    
    
    @property
    def hdfm_filewritemode(self):
        return self.pv_record_map.hdfm_filewritemode
    
    @hdfm_filewritemode.setter
    def hdfm_filewritemode(self, value):
        self.pv_record_map.hdfm_filewritemode = value
    
    
    @property
    def hdfm_numcapture(self):
        return self.pv_record_map.hdfm_numcapture
    
    @hdfm_numcapture.setter
    def hdfm_numcapture(self, value):
        self.pv_record_map.hdfm_numcapture = value
    
    
    @property
    def hdfm_numcapture_rbv(self):
        return self.pv_record_map.hdfm_numcapture_rbv
    
    
    @property
    def hdfm_writefile(self):
        return self.pv_record_map.hdfm_writefile
    
    
    @property
    def hdfm_writefile_rbv(self):
        return self.pv_record_map.hdfm_writefile_rbv
    
    
    @property
    def hdfm_writemessage(self):
        return self.pv_record_map.hdfm_writemessage
    
    
    @property
    def hdfm_writestatus(self):
        return self.pv_record_map.hdfm_writestatus
    
    
    @property
    def hdf_autosave(self):
        return self.pv_record_map.hdf_autosave
    
    @hdf_autosave.setter
    def hdf_autosave(self, value):
        self.pv_record_map.hdf_autosave = value
    
    
    @property
    def hdf_capture(self):
        return self.pv_record_map.hdf_capture
    
    @hdf_capture.setter
    def hdf_capture(self, value):
        self.pv_record_map.hdf_capture = value
    
    
    @property
    def hdf_capture_disv(self):
        return self.pv_record_map.hdf_capture_disv
    
    @hdf_capture_disv.setter
    def hdf_capture_disv(self, value):
        self.pv_record_map.hdf_capture_disv = value
    
    
    @property
    def hdf_capture_rbv(self):
        return self.pv_record_map.hdf_capture_rbv
    
    
    @property
    def hdf_filename(self):
        return self.pv_record_map.hdf_filename
    
    
    @property
    def hdf_filename_rbv(self):
        return self.pv_record_map.hdf_filename_rbv
    
    
    @property
    def hdf_filenumber(self):
        return self.pv_record_map.hdf_filenumber
    
    
    @property
    def hdf_filenumber_rbv(self):
        return self.pv_record_map.hdf_filenumber_rbv
    
    
    @property
    def hdf_filepath(self):
        return self.pv_record_map.hdf_filepath
    
    
    @property
    def hdf_filepath_rbv(self):
        return self.pv_record_map.hdf_filepath_rbv
    
    
    @property
    def hdf_filewritemode(self):
        return self.pv_record_map.hdf_filewritemode
    
    @hdf_filewritemode.setter
    def hdf_filewritemode(self, value):
        self.pv_record_map.hdf_filewritemode = value
    
    
    @property
    def hdf_numcapture(self):
        return self.pv_record_map.hdf_numcapture
    
    @hdf_numcapture.setter
    def hdf_numcapture(self, value):
        self.pv_record_map.hdf_numcapture = value
    
    
    @property
    def hdf_numcapture_rbv(self):
        return self.pv_record_map.hdf_numcapture_rbv
    
    
    @property
    def hdf_writefile(self):
        return self.pv_record_map.hdf_writefile
    
    
    @property
    def hdf_writefile_rbv(self):
        return self.pv_record_map.hdf_writefile_rbv
    
    
    @property
    def hdf_writemessage(self):
        return self.pv_record_map.hdf_writemessage
    
    
    @property
    def hdf_writestatus(self):
        return self.pv_record_map.hdf_writestatus
    
    
    @property
    def init_buffer(self):
        return self.pv_record_map.init_buffer
    
    @init_buffer.setter
    def init_buffer(self, value):
        self.pv_record_map.init_buffer = value
    
    
    @property
    def led_off(self):
        return self.pv_record_map.led_off
    
    @led_off.setter
    def led_off(self, value):
        self.pv_record_map.led_off = value
    
    
    @property
    def led_on(self):
        return self.pv_record_map.led_on
    
    @led_on.setter
    def led_on(self, value):
        self.pv_record_map.led_on = value
    
    
    @property
    def led_sta(self):
        return self.pv_record_map.led_sta
    
    
    @property
    def magick_autosave(self):
        return self.pv_record_map.magick_autosave
    
    @magick_autosave.setter
    def magick_autosave(self, value):
        self.pv_record_map.magick_autosave = value
    
    
    @property
    def magick_capture(self):
        return self.pv_record_map.magick_capture
    
    @magick_capture.setter
    def magick_capture(self, value):
        self.pv_record_map.magick_capture = value
    
    
    @property
    def magick_capture_disv(self):
        return self.pv_record_map.magick_capture_disv
    
    @magick_capture_disv.setter
    def magick_capture_disv(self, value):
        self.pv_record_map.magick_capture_disv = value
    
    
    @property
    def magick_capture_rbv(self):
        return self.pv_record_map.magick_capture_rbv
    
    
    @property
    def magick_filename(self):
        return self.pv_record_map.magick_filename
    
    
    @property
    def magick_filename_rbv(self):
        return self.pv_record_map.magick_filename_rbv
    
    
    @property
    def magick_filenumber(self):
        return self.pv_record_map.magick_filenumber
    
    
    @property
    def magick_filenumber_rbv(self):
        return self.pv_record_map.magick_filenumber_rbv
    
    
    @property
    def magick_filepath(self):
        return self.pv_record_map.magick_filepath
    
    
    @property
    def magick_filepath_rbv(self):
        return self.pv_record_map.magick_filepath_rbv
    
    
    @property
    def magick_filewritemode(self):
        return self.pv_record_map.magick_filewritemode
    
    @magick_filewritemode.setter
    def magick_filewritemode(self, value):
        self.pv_record_map.magick_filewritemode = value
    
    
    @property
    def magick_numcapture(self):
        return self.pv_record_map.magick_numcapture
    
    @magick_numcapture.setter
    def magick_numcapture(self, value):
        self.pv_record_map.magick_numcapture = value
    
    
    @property
    def magick_numcapture_rbv(self):
        return self.pv_record_map.magick_numcapture_rbv
    
    
    @property
    def magick_writefile(self):
        return self.pv_record_map.magick_writefile
    
    
    @property
    def magick_writefile_rbv(self):
        return self.pv_record_map.magick_writefile_rbv
    
    
    @property
    def magick_writemessage(self):
        return self.pv_record_map.magick_writemessage
    
    
    @property
    def magick_writestatus(self):
        return self.pv_record_map.magick_writestatus
    
    
    @property
    def roi1_imagedata_rbv(self):
        return self.pv_record_map.roi1_imagedata_rbv
    
    
    @property
    def roi1_minx(self):
        return self.pv_record_map.roi1_minx
    
    
    @property
    def roi1_minx_rbv(self):
        return self.pv_record_map.roi1_minx_rbv
    
    
    @property
    def roi1_miny(self):
        return self.pv_record_map.roi1_miny
    
    
    @property
    def roi1_miny_rbv(self):
        return self.pv_record_map.roi1_miny_rbv
    
    
    @property
    def roi1_sizex(self):
        return self.pv_record_map.roi1_sizex
    
    
    @property
    def roi1_sizex_rbv(self):
        return self.pv_record_map.roi1_sizex_rbv
    
    
    @property
    def roi1_sizey(self):
        return self.pv_record_map.roi1_sizey
    
    
    @property
    def roi1_sizey_rbv(self):
        return self.pv_record_map.roi1_sizey_rbv
    
    
    @property
    def roiandmask_setx(self):
        return self.pv_record_map.roiandmask_setx
    
    
    @property
    def roiandmask_setxrad(self):
        return self.pv_record_map.roiandmask_setxrad
    
    
    @property
    def roiandmask_sety(self):
        return self.pv_record_map.roiandmask_sety
    
    
    @property
    def roiandmask_setyrad(self):
        return self.pv_record_map.roiandmask_setyrad
    
    
    @property
    def reset_buffer(self):
        return self.pv_record_map.reset_buffer
    
    @reset_buffer.setter
    def reset_buffer(self, value):
        self.pv_record_map.reset_buffer = value
    
    
    @property
    def save(self):
        return self.pv_record_map.save
    
    @save.setter
    def save(self, value):
        self.pv_record_map.save = value
    
    
    @property
    def save_buffer(self):
        return self.pv_record_map.save_buffer
    
    @save_buffer.setter
    def save_buffer(self, value):
        self.pv_record_map.save_buffer = value
    
    
    @property
    def save_buffer_path_initialise(self):
        return self.pv_record_map.save_buffer_path_initialise
    
    @save_buffer_path_initialise.setter
    def save_buffer_path_initialise(self, value):
        self.pv_record_map.save_buffer_path_initialise = value
    
    
    @property
    def save_path_initialise(self):
        return self.pv_record_map.save_path_initialise
    
    @save_path_initialise.setter
    def save_path_initialise(self, value):
        self.pv_record_map.save_path_initialise = value
    
    


class CameraProperties(Properties):
    """
    Class for defining camera-specific properties.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Properties`
    """

    
    ARRAY_DATA_NUM_PIX_X: int
    """"""
    
    ARRAY_DATA_NUM_PIX_Y: int
    """"""
    
    ARRAY_DATA_X_PIX_2_MM: float
    """"""
    
    ARRAY_DATA_Y_PIX_2_MM: float
    """"""
    
    CAM_TYPE: str
    """"""
    
    HAS_LED: bool
    """"""
    
    IMAGE_FLIP_LR: bool
    """"""
    
    IMAGE_FLIP_UD: bool
    """"""
    
    IMAGE_ROTATION: int
    """"""
    
    IOC: list
    """"""
    
    IP_ADDRESS_STREAM: str
    """"""
    
    MAX_BIT_DEPTH: int
    """"""
    
    PIX_2_MM_RATIO_DEF: float
    """"""
    
    SCREEN_NAME: str
    """"""
    
    USE_MASK_RAD_LIMITS: bool
    """"""
    
    timeout: float
    """"""
    

    def __init__(self, *args, **kwargs):
        super(
            CameraProperties,
            self,
        ).__init__(
            *args,
            **kwargs,
        )

    
    @property
    def ARRAY_DATA_NUM_PIX_X(self):
        return self.ARRAY_DATA_NUM_PIX_X
    
    @property
    def ARRAY_DATA_NUM_PIX_Y(self):
        return self.ARRAY_DATA_NUM_PIX_Y
    
    @property
    def ARRAY_DATA_X_PIX_2_MM(self):
        return self.ARRAY_DATA_X_PIX_2_MM
    
    @property
    def ARRAY_DATA_Y_PIX_2_MM(self):
        return self.ARRAY_DATA_Y_PIX_2_MM
    
    @property
    def CAM_TYPE(self):
        return self.CAM_TYPE
    
    @property
    def HAS_LED(self):
        return self.HAS_LED
    
    @property
    def IMAGE_FLIP_LR(self):
        return self.IMAGE_FLIP_LR
    
    @property
    def IMAGE_FLIP_UD(self):
        return self.IMAGE_FLIP_UD
    
    @property
    def IMAGE_ROTATION(self):
        return self.IMAGE_ROTATION
    
    @property
    def IOC(self):
        return self.IOC
    
    @property
    def IP_ADDRESS_STREAM(self):
        return self.IP_ADDRESS_STREAM
    
    @property
    def MAX_BIT_DEPTH(self):
        return self.MAX_BIT_DEPTH
    
    @property
    def PIX_2_MM_RATIO_DEF(self):
        return self.PIX_2_MM_RATIO_DEF
    
    @property
    def SCREEN_NAME(self):
        return self.SCREEN_NAME
    
    @property
    def USE_MASK_RAD_LIMITS(self):
        return self.USE_MASK_RAD_LIMITS
    
    @property
    def timeout(self):
        return self.timeout
    

    
    @property
    def ARRAY_DATA_X_PIX_2_MM(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.ARRAY_DATA_X_PIX_2_MM

    @ARRAY_DATA_X_PIX_2_MM.setter
    def ARRAY_DATA_X_PIX_2_MM(self, value: float) -> None:
        self.ARRAY_DATA_X_PIX_2_MM = value
    
    @property
    def ARRAY_DATA_Y_PIX_2_MM(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.ARRAY_DATA_Y_PIX_2_MM

    @ARRAY_DATA_Y_PIX_2_MM.setter
    def ARRAY_DATA_Y_PIX_2_MM(self, value: float) -> None:
        self.ARRAY_DATA_Y_PIX_2_MM = value
    
    @property
    def PIX_2_MM_RATIO_DEF(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.PIX_2_MM_RATIO_DEF

    @PIX_2_MM_RATIO_DEF.setter
    def PIX_2_MM_RATIO_DEF(self, value: float) -> None:
        self.PIX_2_MM_RATIO_DEF = value
    
    @property
    def timeout(self) -> float:
        """
        

        :getter: Gets the value.
        :setter: Sets the value.
        :type: float
        """
        return self.timeout

    @timeout.setter
    def timeout(self, value: float) -> None:
        self.timeout = value
    

class Camera(Hardware):
    """
    Middle layer class for interacting with a specific camera object.

    Inherits from:
        :class:`~CATAP.common.machine.hardware.Hardware`
    """

    controls_information: SerializeAsAny[CameraControlsInformation]
    """Controls information pertaining to this camera
    (see :class:`~CATAP.common.machine.pv_utils.ControlsInformation`)"""
    properties: SerializeAsAny[CameraProperties]
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
            Camera,
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
    def validate_controls_information(cls, v: Any) -> CameraControlsInformation:
        try:
            return CameraControlsInformation(
                is_virtual=cls.is_virtual,
                connect_on_creation=cls.connect_on_creation,
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate controls_information: {e}")

    @field_validator("properties", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> CameraProperties:
        try:
            return CameraProperties(
                **v,
            )
        except Exception as e:
            raise ValueError(f"Failed to validate properties: {e}")

    
    @property
    def ana_avgintensity_rbv(self):
        return self.controls_information.ana_avgintensity_rbv
    
    
    @property
    def ana_cpu_cropsubmask_rbv(self):
        return self.controls_information.ana_cpu_cropsubmask_rbv
    
    
    @property
    def ana_cpu_dot_rbv(self):
        return self.controls_information.ana_cpu_dot_rbv
    
    
    @property
    def ana_cpu_npoint_rbv(self):
        return self.controls_information.ana_cpu_npoint_rbv
    
    
    @property
    def ana_cpu_rbv(self):
        return self.controls_information.ana_cpu_rbv
    
    
    @property
    def ana_centerx(self):
        return self.controls_information.ana_centerx
    
    
    @property
    def ana_centerx_rbv(self):
        return self.controls_information.ana_centerx_rbv
    
    
    @property
    def ana_centery(self):
        return self.controls_information.ana_centery
    
    
    @property
    def ana_centery_rbv(self):
        return self.controls_information.ana_centery_rbv
    
    
    @property
    def ana_covxypix_rbv(self):
        return self.controls_information.ana_covxypix_rbv
    
    
    @property
    def ana_covxy_rbv(self):
        return self.controls_information.ana_covxy_rbv
    
    
    @property
    def ana_enablecallbacks(self):
        return self.controls_information.ana_enablecallbacks
    
    @ana_enablecallbacks.setter
    def ana_enablecallbacks(self, value):
        self.controls_information.ana_enablecallbacks = value
    
    
    @property
    def ana_enablecallbacks_rbv(self):
        return self.controls_information.ana_enablecallbacks_rbv
    
    
    @property
    def ana_floorlevel(self):
        return self.controls_information.ana_floorlevel
    
    
    @property
    def ana_floorlevel_rbv(self):
        return self.controls_information.ana_floorlevel_rbv
    
    
    @property
    def ana_flooredpercent_rbv(self):
        return self.controls_information.ana_flooredpercent_rbv
    
    
    @property
    def ana_flooredpoints_rbv(self):
        return self.controls_information.ana_flooredpoints_rbv
    
    
    @property
    def ana_intensity_rbv(self):
        return self.controls_information.ana_intensity_rbv
    
    
    @property
    def ana_mmresults_rbv(self):
        return self.controls_information.ana_mmresults_rbv
    
    
    @property
    def ana_maskheight_rbv(self):
        return self.controls_information.ana_maskheight_rbv
    
    
    @property
    def ana_maskwidth_rbv(self):
        return self.controls_information.ana_maskwidth_rbv
    
    
    @property
    def ana_maskxcenter(self):
        return self.controls_information.ana_maskxcenter
    
    
    @property
    def ana_maskxcenter_rbv(self):
        return self.controls_information.ana_maskxcenter_rbv
    
    
    @property
    def ana_maskxrad(self):
        return self.controls_information.ana_maskxrad
    
    
    @property
    def ana_maskxrad_rbv(self):
        return self.controls_information.ana_maskxrad_rbv
    
    
    @property
    def ana_maskycenter(self):
        return self.controls_information.ana_maskycenter
    
    
    @property
    def ana_maskycenter_rbv(self):
        return self.controls_information.ana_maskycenter_rbv
    
    
    @property
    def ana_maskyrad(self):
        return self.controls_information.ana_maskyrad
    
    
    @property
    def ana_maskyrad_rbv(self):
        return self.controls_information.ana_maskyrad_rbv
    
    
    @property
    def ana_npointstepsize(self):
        return self.controls_information.ana_npointstepsize
    
    
    @property
    def ana_npointstepsize_rbv(self):
        return self.controls_information.ana_npointstepsize_rbv
    
    
    @property
    def ana_newbkgrnd(self):
        return self.controls_information.ana_newbkgrnd
    
    
    @property
    def ana_newbkgrnd_rbv(self):
        return self.controls_information.ana_newbkgrnd_rbv
    
    
    @property
    def ana_overlay_1_cross(self):
        return self.controls_information.ana_overlay_1_cross
    
    
    @property
    def ana_overlay_1_cross_rbv(self):
        return self.controls_information.ana_overlay_1_cross_rbv
    
    
    @property
    def ana_overlay_2_result(self):
        return self.controls_information.ana_overlay_2_result
    
    
    @property
    def ana_overlay_2_result_rbv(self):
        return self.controls_information.ana_overlay_2_result_rbv
    
    
    @property
    def ana_overlay_3_mask(self):
        return self.controls_information.ana_overlay_3_mask
    
    
    @property
    def ana_overlay_3_mask_rbv(self):
        return self.controls_information.ana_overlay_3_mask_rbv
    
    
    @property
    def ana_pixh_rbv(self):
        return self.controls_information.ana_pixh_rbv
    
    
    @property
    def ana_pixmm(self):
        return self.controls_information.ana_pixmm
    
    
    @property
    def ana_pixmm_rbv(self):
        return self.controls_information.ana_pixmm_rbv
    
    
    @property
    def ana_pixw_rbv(self):
        return self.controls_information.ana_pixw_rbv
    
    
    @property
    def ana_pixelresults_rbv(self):
        return self.controls_information.ana_pixelresults_rbv
    
    
    @property
    def ana_sigmaxpix_rbv(self):
        return self.controls_information.ana_sigmaxpix_rbv
    
    
    @property
    def ana_sigmax_rbv(self):
        return self.controls_information.ana_sigmax_rbv
    
    
    @property
    def ana_sigmaypix_rbv(self):
        return self.controls_information.ana_sigmaypix_rbv
    
    
    @property
    def ana_sigmay_rbv(self):
        return self.controls_information.ana_sigmay_rbv
    
    
    @property
    def ana_usebkgrnd(self):
        return self.controls_information.ana_usebkgrnd
    
    
    @property
    def ana_usebkgrnd_rbv(self):
        return self.controls_information.ana_usebkgrnd_rbv
    
    
    @property
    def ana_usefloor(self):
        return self.controls_information.ana_usefloor
    
    
    @property
    def ana_usefloor_rbv(self):
        return self.controls_information.ana_usefloor_rbv
    
    
    @property
    def ana_usenpoint(self):
        return self.controls_information.ana_usenpoint
    
    
    @property
    def ana_usenpoint_rbv(self):
        return self.controls_information.ana_usenpoint_rbv
    
    
    @property
    def ana_xpix_rbv(self):
        return self.controls_information.ana_xpix_rbv
    
    
    @property
    def ana_x_rbv(self):
        return self.controls_information.ana_x_rbv
    
    
    @property
    def ana_ypix_rbv(self):
        return self.controls_information.ana_ypix_rbv
    
    
    @property
    def ana_y_rbv(self):
        return self.controls_information.ana_y_rbv
    
    
    @property
    def buffer_status(self):
        return self.controls_information.buffer_status
    
    
    @property
    def cam1_arraydata(self):
        return self.controls_information.cam1_arraydata
    
    
    @property
    def cam2_arraydata(self):
        return self.controls_information.cam2_arraydata
    
    
    @property
    def cam_acquireperiod_rbv(self):
        return self.controls_information.cam_acquireperiod_rbv
    
    
    @property
    def cam_acquiretime_rbv(self):
        return self.controls_information.cam_acquiretime_rbv
    
    
    @property
    def cam_acquire_rbv(self):
        return self.controls_information.cam_acquire_rbv
    
    
    @property
    def cam_active_count(self):
        return self.controls_information.cam_active_count
    
    
    @property
    def cam_active_limit(self):
        return self.controls_information.cam_active_limit
    
    
    @property
    def cam_arrayrate_rbv(self):
        return self.controls_information.cam_arrayrate_rbv
    
    
    @property
    def cam_start_acquire(self):
        return self.controls_information.cam_start_acquire
    
    @cam_start_acquire.setter
    def cam_start_acquire(self, value):
        self.controls_information.cam_start_acquire = value
    
    
    @property
    def cam_stop_acquire(self):
        return self.controls_information.cam_stop_acquire
    
    @cam_stop_acquire.setter
    def cam_stop_acquire(self, value):
        self.controls_information.cam_stop_acquire = value
    
    
    @property
    def cam_temperature_rbv(self):
        return self.controls_information.cam_temperature_rbv
    
    
    @property
    def hdfb_autosave(self):
        return self.controls_information.hdfb_autosave
    
    @hdfb_autosave.setter
    def hdfb_autosave(self, value):
        self.controls_information.hdfb_autosave = value
    
    
    @property
    def hdfb_buffer_filenumber(self):
        return self.controls_information.hdfb_buffer_filenumber
    
    
    @property
    def hdfb_buffer_filenumber_rbv(self):
        return self.controls_information.hdfb_buffer_filenumber_rbv
    
    
    @property
    def hdfb_capture(self):
        return self.controls_information.hdfb_capture
    
    @hdfb_capture.setter
    def hdfb_capture(self, value):
        self.controls_information.hdfb_capture = value
    
    
    @property
    def hdfb_capture_disv(self):
        return self.controls_information.hdfb_capture_disv
    
    @hdfb_capture_disv.setter
    def hdfb_capture_disv(self, value):
        self.controls_information.hdfb_capture_disv = value
    
    
    @property
    def hdfb_capture_rbv(self):
        return self.controls_information.hdfb_capture_rbv
    
    
    @property
    def hdfb_filename(self):
        return self.controls_information.hdfb_filename
    
    
    @property
    def hdfb_filename_rbv(self):
        return self.controls_information.hdfb_filename_rbv
    
    
    @property
    def hdfb_filenumber(self):
        return self.controls_information.hdfb_filenumber
    
    
    @property
    def hdfb_filenumber_rbv(self):
        return self.controls_information.hdfb_filenumber_rbv
    
    
    @property
    def hdfb_filepath(self):
        return self.controls_information.hdfb_filepath
    
    
    @property
    def hdfb_filepath_rbv(self):
        return self.controls_information.hdfb_filepath_rbv
    
    
    @property
    def hdfb_filewritemode(self):
        return self.controls_information.hdfb_filewritemode
    
    @hdfb_filewritemode.setter
    def hdfb_filewritemode(self, value):
        self.controls_information.hdfb_filewritemode = value
    
    
    @property
    def hdfb_numcapture(self):
        return self.controls_information.hdfb_numcapture
    
    @hdfb_numcapture.setter
    def hdfb_numcapture(self, value):
        self.controls_information.hdfb_numcapture = value
    
    
    @property
    def hdfb_numcapture_rbv(self):
        return self.controls_information.hdfb_numcapture_rbv
    
    
    @property
    def hdfb_numcaptured_rbv(self):
        return self.controls_information.hdfb_numcaptured_rbv
    
    
    @property
    def hdfb_numimagescached_rbv(self):
        return self.controls_information.hdfb_numimagescached_rbv
    
    
    @property
    def hdfb_postcount(self):
        return self.controls_information.hdfb_postcount
    
    @hdfb_postcount.setter
    def hdfb_postcount(self, value):
        self.controls_information.hdfb_postcount = value
    
    
    @property
    def hdfb_precount(self):
        return self.controls_information.hdfb_precount
    
    @hdfb_precount.setter
    def hdfb_precount(self, value):
        self.controls_information.hdfb_precount = value
    
    
    @property
    def hdfb_writefile(self):
        return self.controls_information.hdfb_writefile
    
    
    @property
    def hdfb_writefile_rbv(self):
        return self.controls_information.hdfb_writefile_rbv
    
    
    @property
    def hdfb_writemessage(self):
        return self.controls_information.hdfb_writemessage
    
    
    @property
    def hdfb_writestatus(self):
        return self.controls_information.hdfb_writestatus
    
    
    @property
    def hdfb_image_buffer_filename(self):
        return self.controls_information.hdfb_image_buffer_filename
    
    
    @property
    def hdfb_image_buffer_filename_rbv(self):
        return self.controls_information.hdfb_image_buffer_filename_rbv
    
    
    @property
    def hdfb_image_buffer_filepath(self):
        return self.controls_information.hdfb_image_buffer_filepath
    
    
    @property
    def hdfb_image_buffer_filepath_rbv(self):
        return self.controls_information.hdfb_image_buffer_filepath_rbv
    
    
    @property
    def hdfb_image_buffer_trigger(self):
        return self.controls_information.hdfb_image_buffer_trigger
    
    
    @property
    def hdfm_autosave(self):
        return self.controls_information.hdfm_autosave
    
    @hdfm_autosave.setter
    def hdfm_autosave(self, value):
        self.controls_information.hdfm_autosave = value
    
    
    @property
    def hdfm_capture(self):
        return self.controls_information.hdfm_capture
    
    @hdfm_capture.setter
    def hdfm_capture(self, value):
        self.controls_information.hdfm_capture = value
    
    
    @property
    def hdfm_capture_disv(self):
        return self.controls_information.hdfm_capture_disv
    
    @hdfm_capture_disv.setter
    def hdfm_capture_disv(self, value):
        self.controls_information.hdfm_capture_disv = value
    
    
    @property
    def hdfm_capture_rbv(self):
        return self.controls_information.hdfm_capture_rbv
    
    
    @property
    def hdfm_filename(self):
        return self.controls_information.hdfm_filename
    
    
    @property
    def hdfm_filename_rbv(self):
        return self.controls_information.hdfm_filename_rbv
    
    
    @property
    def hdfm_filenumber(self):
        return self.controls_information.hdfm_filenumber
    
    
    @property
    def hdfm_filenumber_rbv(self):
        return self.controls_information.hdfm_filenumber_rbv
    
    
    @property
    def hdfm_filepath(self):
        return self.controls_information.hdfm_filepath
    
    
    @property
    def hdfm_filepath_rbv(self):
        return self.controls_information.hdfm_filepath_rbv
    
    
    @property
    def hdfm_filewritemode(self):
        return self.controls_information.hdfm_filewritemode
    
    @hdfm_filewritemode.setter
    def hdfm_filewritemode(self, value):
        self.controls_information.hdfm_filewritemode = value
    
    
    @property
    def hdfm_numcapture(self):
        return self.controls_information.hdfm_numcapture
    
    @hdfm_numcapture.setter
    def hdfm_numcapture(self, value):
        self.controls_information.hdfm_numcapture = value
    
    
    @property
    def hdfm_numcapture_rbv(self):
        return self.controls_information.hdfm_numcapture_rbv
    
    
    @property
    def hdfm_writefile(self):
        return self.controls_information.hdfm_writefile
    
    
    @property
    def hdfm_writefile_rbv(self):
        return self.controls_information.hdfm_writefile_rbv
    
    
    @property
    def hdfm_writemessage(self):
        return self.controls_information.hdfm_writemessage
    
    
    @property
    def hdfm_writestatus(self):
        return self.controls_information.hdfm_writestatus
    
    
    @property
    def hdf_autosave(self):
        return self.controls_information.hdf_autosave
    
    @hdf_autosave.setter
    def hdf_autosave(self, value):
        self.controls_information.hdf_autosave = value
    
    
    @property
    def hdf_capture(self):
        return self.controls_information.hdf_capture
    
    @hdf_capture.setter
    def hdf_capture(self, value):
        self.controls_information.hdf_capture = value
    
    
    @property
    def hdf_capture_disv(self):
        return self.controls_information.hdf_capture_disv
    
    @hdf_capture_disv.setter
    def hdf_capture_disv(self, value):
        self.controls_information.hdf_capture_disv = value
    
    
    @property
    def hdf_capture_rbv(self):
        return self.controls_information.hdf_capture_rbv
    
    
    @property
    def hdf_filename(self):
        return self.controls_information.hdf_filename
    
    
    @property
    def hdf_filename_rbv(self):
        return self.controls_information.hdf_filename_rbv
    
    
    @property
    def hdf_filenumber(self):
        return self.controls_information.hdf_filenumber
    
    
    @property
    def hdf_filenumber_rbv(self):
        return self.controls_information.hdf_filenumber_rbv
    
    
    @property
    def hdf_filepath(self):
        return self.controls_information.hdf_filepath
    
    
    @property
    def hdf_filepath_rbv(self):
        return self.controls_information.hdf_filepath_rbv
    
    
    @property
    def hdf_filewritemode(self):
        return self.controls_information.hdf_filewritemode
    
    @hdf_filewritemode.setter
    def hdf_filewritemode(self, value):
        self.controls_information.hdf_filewritemode = value
    
    
    @property
    def hdf_numcapture(self):
        return self.controls_information.hdf_numcapture
    
    @hdf_numcapture.setter
    def hdf_numcapture(self, value):
        self.controls_information.hdf_numcapture = value
    
    
    @property
    def hdf_numcapture_rbv(self):
        return self.controls_information.hdf_numcapture_rbv
    
    
    @property
    def hdf_writefile(self):
        return self.controls_information.hdf_writefile
    
    
    @property
    def hdf_writefile_rbv(self):
        return self.controls_information.hdf_writefile_rbv
    
    
    @property
    def hdf_writemessage(self):
        return self.controls_information.hdf_writemessage
    
    
    @property
    def hdf_writestatus(self):
        return self.controls_information.hdf_writestatus
    
    
    @property
    def init_buffer(self):
        return self.controls_information.init_buffer
    
    @init_buffer.setter
    def init_buffer(self, value):
        self.controls_information.init_buffer = value
    
    
    @property
    def led_off(self):
        return self.controls_information.led_off
    
    @led_off.setter
    def led_off(self, value):
        self.controls_information.led_off = value
    
    
    @property
    def led_on(self):
        return self.controls_information.led_on
    
    @led_on.setter
    def led_on(self, value):
        self.controls_information.led_on = value
    
    
    @property
    def led_sta(self):
        return self.controls_information.led_sta
    
    
    @property
    def magick_autosave(self):
        return self.controls_information.magick_autosave
    
    @magick_autosave.setter
    def magick_autosave(self, value):
        self.controls_information.magick_autosave = value
    
    
    @property
    def magick_capture(self):
        return self.controls_information.magick_capture
    
    @magick_capture.setter
    def magick_capture(self, value):
        self.controls_information.magick_capture = value
    
    
    @property
    def magick_capture_disv(self):
        return self.controls_information.magick_capture_disv
    
    @magick_capture_disv.setter
    def magick_capture_disv(self, value):
        self.controls_information.magick_capture_disv = value
    
    
    @property
    def magick_capture_rbv(self):
        return self.controls_information.magick_capture_rbv
    
    
    @property
    def magick_filename(self):
        return self.controls_information.magick_filename
    
    
    @property
    def magick_filename_rbv(self):
        return self.controls_information.magick_filename_rbv
    
    
    @property
    def magick_filenumber(self):
        return self.controls_information.magick_filenumber
    
    
    @property
    def magick_filenumber_rbv(self):
        return self.controls_information.magick_filenumber_rbv
    
    
    @property
    def magick_filepath(self):
        return self.controls_information.magick_filepath
    
    
    @property
    def magick_filepath_rbv(self):
        return self.controls_information.magick_filepath_rbv
    
    
    @property
    def magick_filewritemode(self):
        return self.controls_information.magick_filewritemode
    
    @magick_filewritemode.setter
    def magick_filewritemode(self, value):
        self.controls_information.magick_filewritemode = value
    
    
    @property
    def magick_numcapture(self):
        return self.controls_information.magick_numcapture
    
    @magick_numcapture.setter
    def magick_numcapture(self, value):
        self.controls_information.magick_numcapture = value
    
    
    @property
    def magick_numcapture_rbv(self):
        return self.controls_information.magick_numcapture_rbv
    
    
    @property
    def magick_writefile(self):
        return self.controls_information.magick_writefile
    
    
    @property
    def magick_writefile_rbv(self):
        return self.controls_information.magick_writefile_rbv
    
    
    @property
    def magick_writemessage(self):
        return self.controls_information.magick_writemessage
    
    
    @property
    def magick_writestatus(self):
        return self.controls_information.magick_writestatus
    
    
    @property
    def roi1_imagedata_rbv(self):
        return self.controls_information.roi1_imagedata_rbv
    
    
    @property
    def roi1_minx(self):
        return self.controls_information.roi1_minx
    
    
    @property
    def roi1_minx_rbv(self):
        return self.controls_information.roi1_minx_rbv
    
    
    @property
    def roi1_miny(self):
        return self.controls_information.roi1_miny
    
    
    @property
    def roi1_miny_rbv(self):
        return self.controls_information.roi1_miny_rbv
    
    
    @property
    def roi1_sizex(self):
        return self.controls_information.roi1_sizex
    
    
    @property
    def roi1_sizex_rbv(self):
        return self.controls_information.roi1_sizex_rbv
    
    
    @property
    def roi1_sizey(self):
        return self.controls_information.roi1_sizey
    
    
    @property
    def roi1_sizey_rbv(self):
        return self.controls_information.roi1_sizey_rbv
    
    
    @property
    def roiandmask_setx(self):
        return self.controls_information.roiandmask_setx
    
    
    @property
    def roiandmask_setxrad(self):
        return self.controls_information.roiandmask_setxrad
    
    
    @property
    def roiandmask_sety(self):
        return self.controls_information.roiandmask_sety
    
    
    @property
    def roiandmask_setyrad(self):
        return self.controls_information.roiandmask_setyrad
    
    
    @property
    def reset_buffer(self):
        return self.controls_information.reset_buffer
    
    @reset_buffer.setter
    def reset_buffer(self, value):
        self.controls_information.reset_buffer = value
    
    
    @property
    def save(self):
        return self.controls_information.save
    
    @save.setter
    def save(self, value):
        self.controls_information.save = value
    
    
    @property
    def save_buffer(self):
        return self.controls_information.save_buffer
    
    @save_buffer.setter
    def save_buffer(self, value):
        self.controls_information.save_buffer = value
    
    
    @property
    def save_buffer_path_initialise(self):
        return self.controls_information.save_buffer_path_initialise
    
    @save_buffer_path_initialise.setter
    def save_buffer_path_initialise(self, value):
        self.controls_information.save_buffer_path_initialise = value
    
    
    @property
    def save_path_initialise(self):
        return self.controls_information.save_path_initialise
    
    @save_path_initialise.setter
    def save_path_initialise(self, value):
        self.controls_information.save_path_initialise = value
    
    

class CameraFactory(Factory):
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
        super(CameraFactory, self).__init__(
            is_virtual=is_virtual,
            hardware_type=Camera,
            connect_on_creation=connect_on_creation,
            areas=areas,
        )

    def get_camera(self, name: Union[str, List[str]] = None) -> Camera:
        """
        Returns the camera object for the given name(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str

        :return: Camera object(s).
        :rtype: :class:`~CATAP.laser.components.camera.Camera`
        or Dict[str: :class:`~CATAP.laser.components.camera.Camera`]
        """
        return self.get_hardware(name)

    
    def ana_avgintensity_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_avgintensity_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_AvgIntensity_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_avgintensity_rbv)
    
    def ana_cpu_cropsubmask_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_cpu_cropsubmask_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_CPU_CropSubMask_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_cpu_cropsubmask_rbv)
    
    def ana_cpu_dot_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_cpu_dot_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_CPU_Dot_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_cpu_dot_rbv)
    
    def ana_cpu_npoint_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_cpu_npoint_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_CPU_Npoint_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_cpu_npoint_rbv)
    
    def ana_cpu_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_cpu_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_CPU_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_cpu_rbv)
    
    def ana_centerx(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_centerx' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_CenterX' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_centerx)
    
    def ana_centerx_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_centerx_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_CenterX_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_centerx_rbv)
    
    def ana_centery(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_centery' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_CenterY' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_centery)
    
    def ana_centery_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_centery_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_CenterY_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_centery_rbv)
    
    def ana_covxypix_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_covxypix_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_CovXYPix_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_covxypix_rbv)
    
    def ana_covxy_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_covxy_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_CovXY_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_covxy_rbv)
    
    def ana_enablecallbacks(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_enablecallbacks' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_EnableCallbacks' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_enablecallbacks)
    
    def ana_enablecallbacks_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_enablecallbacks_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_EnableCallbacks_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_enablecallbacks_rbv)
    
    def ana_floorlevel(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_floorlevel' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_FloorLevel' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_floorlevel)
    
    def ana_floorlevel_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_floorlevel_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_FloorLevel_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_floorlevel_rbv)
    
    def ana_flooredpercent_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_flooredpercent_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_FlooredPercent_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_flooredpercent_rbv)
    
    def ana_flooredpoints_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_flooredpoints_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_FlooredPoints_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_flooredpoints_rbv)
    
    def ana_intensity_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_intensity_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_Intensity_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_intensity_rbv)
    
    def ana_mmresults_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_mmresults_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_MMResults_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_mmresults_rbv)
    
    def ana_maskheight_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_maskheight_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_MaskHeight_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_maskheight_rbv)
    
    def ana_maskwidth_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_maskwidth_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_MaskWidth_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_maskwidth_rbv)
    
    def ana_maskxcenter(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_maskxcenter' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_MaskXCenter' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_maskxcenter)
    
    def ana_maskxcenter_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_maskxcenter_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_MaskXCenter_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_maskxcenter_rbv)
    
    def ana_maskxrad(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_maskxrad' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_MaskXRad' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_maskxrad)
    
    def ana_maskxrad_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_maskxrad_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_MaskXRad_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_maskxrad_rbv)
    
    def ana_maskycenter(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_maskycenter' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_MaskYCenter' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_maskycenter)
    
    def ana_maskycenter_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_maskycenter_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_MaskYCenter_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_maskycenter_rbv)
    
    def ana_maskyrad(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_maskyrad' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_MaskYRad' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_maskyrad)
    
    def ana_maskyrad_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_maskyrad_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_MaskYRad_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_maskyrad_rbv)
    
    def ana_npointstepsize(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_npointstepsize' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_NPointStepSize' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_npointstepsize)
    
    def ana_npointstepsize_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_npointstepsize_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_NPointStepSize_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_npointstepsize_rbv)
    
    def ana_newbkgrnd(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_newbkgrnd' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_NewBkgrnd' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_newbkgrnd)
    
    def ana_newbkgrnd_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_newbkgrnd_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_NewBkgrnd_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_newbkgrnd_rbv)
    
    def ana_overlay_1_cross(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_overlay_1_cross' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_OVERLAY_1_CROSS' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_overlay_1_cross)
    
    def ana_overlay_1_cross_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_overlay_1_cross_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_OVERLAY_1_CROSS_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_overlay_1_cross_rbv)
    
    def ana_overlay_2_result(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_overlay_2_result' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_OVERLAY_2_RESULT' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_overlay_2_result)
    
    def ana_overlay_2_result_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_overlay_2_result_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_OVERLAY_2_RESULT_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_overlay_2_result_rbv)
    
    def ana_overlay_3_mask(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_overlay_3_mask' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_OVERLAY_3_MASK' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_overlay_3_mask)
    
    def ana_overlay_3_mask_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_overlay_3_mask_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_OVERLAY_3_MASK_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_overlay_3_mask_rbv)
    
    def ana_pixh_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_pixh_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_PixH_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_pixh_rbv)
    
    def ana_pixmm(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_pixmm' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_PixMM' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_pixmm)
    
    def ana_pixmm_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_pixmm_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_PixMM_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_pixmm_rbv)
    
    def ana_pixw_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_pixw_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_PixW_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_pixw_rbv)
    
    def ana_pixelresults_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_pixelresults_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_PixelResults_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_pixelresults_rbv)
    
    def ana_sigmaxpix_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_sigmaxpix_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_SigmaXPix_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_sigmaxpix_rbv)
    
    def ana_sigmax_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_sigmax_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_SigmaX_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_sigmax_rbv)
    
    def ana_sigmaypix_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_sigmaypix_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_SigmaYPix_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_sigmaypix_rbv)
    
    def ana_sigmay_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_sigmay_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_SigmaY_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_sigmay_rbv)
    
    def ana_usebkgrnd(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_usebkgrnd' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_UseBkgrnd' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_usebkgrnd)
    
    def ana_usebkgrnd_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_usebkgrnd_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_UseBkgrnd_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_usebkgrnd_rbv)
    
    def ana_usefloor(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_usefloor' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_UseFloor' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_usefloor)
    
    def ana_usefloor_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_usefloor_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_UseFloor_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_usefloor_rbv)
    
    def ana_usenpoint(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_usenpoint' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_UseNPoint' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_usenpoint)
    
    def ana_usenpoint_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_usenpoint_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_UseNPoint_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_usenpoint_rbv)
    
    def ana_xpix_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_xpix_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_XPix_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_xpix_rbv)
    
    def ana_x_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_x_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_X_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_x_rbv)
    
    def ana_ypix_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_ypix_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_YPix_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_ypix_rbv)
    
    def ana_y_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'ana_y_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ANA_Y_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.ana_y_rbv)
    
    def buffer_status(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'buffer_status' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'Buffer_Status' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.buffer_status)
    
    def cam1_arraydata(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'cam1_arraydata' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'CAM1_ArrayData' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam1_arraydata)
    
    def cam2_arraydata(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'cam2_arraydata' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'CAM2_ArrayData' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam2_arraydata)
    
    def cam_acquireperiod_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'cam_acquireperiod_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'CAM_AcquirePeriod_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam_acquireperiod_rbv)
    
    def cam_acquiretime_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'cam_acquiretime_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'CAM_AcquireTime_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam_acquiretime_rbv)
    
    def cam_acquire_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'cam_acquire_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'CAM_Acquire_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam_acquire_rbv)
    
    def cam_active_count(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'cam_active_count' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'CAM_Active_Count' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam_active_count)
    
    def cam_active_limit(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'cam_active_limit' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'CAM_Active_Limit' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam_active_limit)
    
    def cam_arrayrate_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'cam_arrayrate_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'CAM_ArrayRate_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam_arrayrate_rbv)
    
    def cam_start_acquire(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'cam_start_acquire' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'CAM_Start_Acquire' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam_start_acquire)
    
    def cam_stop_acquire(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'cam_stop_acquire' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'CAM_Stop_Acquire' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam_stop_acquire)
    
    def cam_temperature_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'cam_temperature_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'CAM_Temperature_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.cam_temperature_rbv)
    
    def hdfb_autosave(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_autosave' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_AutoSave' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_autosave)
    
    def hdfb_buffer_filenumber(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_buffer_filenumber' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_Buffer_FileNumber' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_buffer_filenumber)
    
    def hdfb_buffer_filenumber_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_buffer_filenumber_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_Buffer_FileNumber_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_buffer_filenumber_rbv)
    
    def hdfb_capture(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_capture' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_Capture' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_capture)
    
    def hdfb_capture_disv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_capture_disv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_Capture_DISV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_capture_disv)
    
    def hdfb_capture_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_capture_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_Capture_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_capture_rbv)
    
    def hdfb_filename(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_filename' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_FileName' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_filename)
    
    def hdfb_filename_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_filename_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_FileName_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_filename_rbv)
    
    def hdfb_filenumber(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_filenumber' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_FileNumber' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_filenumber)
    
    def hdfb_filenumber_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_filenumber_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_FileNumber_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_filenumber_rbv)
    
    def hdfb_filepath(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_filepath' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_FilePath' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_filepath)
    
    def hdfb_filepath_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_filepath_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_FilePath_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_filepath_rbv)
    
    def hdfb_filewritemode(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_filewritemode' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_FileWriteMode' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_filewritemode)
    
    def hdfb_numcapture(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_numcapture' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_NumCapture' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_numcapture)
    
    def hdfb_numcapture_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_numcapture_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_NumCapture_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_numcapture_rbv)
    
    def hdfb_numcaptured_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_numcaptured_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_NumCaptured_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_numcaptured_rbv)
    
    def hdfb_numimagescached_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_numimagescached_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_NumImagesCached_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_numimagescached_rbv)
    
    def hdfb_postcount(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_postcount' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_PostCount' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_postcount)
    
    def hdfb_precount(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_precount' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_PreCount' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_precount)
    
    def hdfb_writefile(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_writefile' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_WriteFile' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_writefile)
    
    def hdfb_writefile_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_writefile_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_WriteFile_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_writefile_rbv)
    
    def hdfb_writemessage(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_writemessage' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_WriteMessage' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_writemessage)
    
    def hdfb_writestatus(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_writestatus' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_WriteStatus' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_writestatus)
    
    def hdfb_image_buffer_filename(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_image_buffer_filename' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_image_buffer_fileName' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_image_buffer_filename)
    
    def hdfb_image_buffer_filename_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_image_buffer_filename_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_image_buffer_fileName_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_image_buffer_filename_rbv)
    
    def hdfb_image_buffer_filepath(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_image_buffer_filepath' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_image_buffer_filePath' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_image_buffer_filepath)
    
    def hdfb_image_buffer_filepath_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_image_buffer_filepath_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_image_buffer_filePath_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_image_buffer_filepath_rbv)
    
    def hdfb_image_buffer_trigger(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfb_image_buffer_trigger' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFB_image_buffer_trigger' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfb_image_buffer_trigger)
    
    def hdfm_autosave(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfm_autosave' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFM_AutoSave' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_autosave)
    
    def hdfm_capture(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfm_capture' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFM_Capture' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_capture)
    
    def hdfm_capture_disv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfm_capture_disv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFM_Capture_DISV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_capture_disv)
    
    def hdfm_capture_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfm_capture_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFM_Capture_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_capture_rbv)
    
    def hdfm_filename(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfm_filename' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFM_FileName' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_filename)
    
    def hdfm_filename_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfm_filename_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFM_FileName_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_filename_rbv)
    
    def hdfm_filenumber(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfm_filenumber' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFM_FileNumber' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_filenumber)
    
    def hdfm_filenumber_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfm_filenumber_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFM_FileNumber_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_filenumber_rbv)
    
    def hdfm_filepath(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfm_filepath' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFM_FilePath' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_filepath)
    
    def hdfm_filepath_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfm_filepath_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFM_FilePath_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_filepath_rbv)
    
    def hdfm_filewritemode(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfm_filewritemode' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFM_FileWriteMode' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_filewritemode)
    
    def hdfm_numcapture(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfm_numcapture' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFM_NumCapture' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_numcapture)
    
    def hdfm_numcapture_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfm_numcapture_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFM_NumCapture_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_numcapture_rbv)
    
    def hdfm_writefile(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfm_writefile' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFM_WriteFile' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_writefile)
    
    def hdfm_writefile_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfm_writefile_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFM_WriteFile_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_writefile_rbv)
    
    def hdfm_writemessage(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfm_writemessage' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFM_WriteMessage' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_writemessage)
    
    def hdfm_writestatus(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdfm_writestatus' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDFM_WriteStatus' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdfm_writestatus)
    
    def hdf_autosave(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdf_autosave' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDF_AutoSave' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_autosave)
    
    def hdf_capture(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdf_capture' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDF_Capture' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_capture)
    
    def hdf_capture_disv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdf_capture_disv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDF_Capture_DISV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_capture_disv)
    
    def hdf_capture_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdf_capture_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDF_Capture_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_capture_rbv)
    
    def hdf_filename(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdf_filename' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDF_FileName' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_filename)
    
    def hdf_filename_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdf_filename_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDF_FileName_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_filename_rbv)
    
    def hdf_filenumber(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdf_filenumber' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDF_FileNumber' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_filenumber)
    
    def hdf_filenumber_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdf_filenumber_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDF_FileNumber_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_filenumber_rbv)
    
    def hdf_filepath(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdf_filepath' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDF_FilePath' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_filepath)
    
    def hdf_filepath_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdf_filepath_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDF_FilePath_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_filepath_rbv)
    
    def hdf_filewritemode(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdf_filewritemode' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDF_FileWriteMode' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_filewritemode)
    
    def hdf_numcapture(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdf_numcapture' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDF_NumCapture' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_numcapture)
    
    def hdf_numcapture_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdf_numcapture_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDF_NumCapture_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_numcapture_rbv)
    
    def hdf_writefile(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdf_writefile' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDF_WriteFile' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_writefile)
    
    def hdf_writefile_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdf_writefile_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDF_WriteFile_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_writefile_rbv)
    
    def hdf_writemessage(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdf_writemessage' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDF_WriteMessage' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_writemessage)
    
    def hdf_writestatus(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'hdf_writestatus' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'HDF_WriteStatus' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.hdf_writestatus)
    
    def init_buffer(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'init_buffer' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'Init_Buffer' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.init_buffer)
    
    def led_off(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'led_off' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'LED_Off' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.led_off)
    
    def led_on(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'led_on' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'LED_On' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.led_on)
    
    def led_sta(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'led_sta' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'LED_Sta' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.led_sta)
    
    def magick_autosave(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'magick_autosave' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'MAGICK_AutoSave' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_autosave)
    
    def magick_capture(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'magick_capture' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'MAGICK_Capture' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_capture)
    
    def magick_capture_disv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'magick_capture_disv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'MAGICK_Capture_DISV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_capture_disv)
    
    def magick_capture_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'magick_capture_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'MAGICK_Capture_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_capture_rbv)
    
    def magick_filename(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'magick_filename' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'MAGICK_FileName' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_filename)
    
    def magick_filename_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'magick_filename_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'MAGICK_FileName_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_filename_rbv)
    
    def magick_filenumber(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'magick_filenumber' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'MAGICK_FileNumber' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_filenumber)
    
    def magick_filenumber_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'magick_filenumber_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'MAGICK_FileNumber_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_filenumber_rbv)
    
    def magick_filepath(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'magick_filepath' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'MAGICK_FilePath' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_filepath)
    
    def magick_filepath_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'magick_filepath_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'MAGICK_FilePath_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_filepath_rbv)
    
    def magick_filewritemode(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'magick_filewritemode' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'MAGICK_FileWriteMode' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_filewritemode)
    
    def magick_numcapture(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'magick_numcapture' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'MAGICK_NumCapture' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_numcapture)
    
    def magick_numcapture_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'magick_numcapture_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'MAGICK_NumCapture_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_numcapture_rbv)
    
    def magick_writefile(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'magick_writefile' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'MAGICK_WriteFile' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_writefile)
    
    def magick_writefile_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'magick_writefile_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'MAGICK_WriteFile_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_writefile_rbv)
    
    def magick_writemessage(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'magick_writemessage' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'MAGICK_WriteMessage' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_writemessage)
    
    def magick_writestatus(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'magick_writestatus' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'MAGICK_WriteStatus' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.magick_writestatus)
    
    def roi1_imagedata_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'roi1_imagedata_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ROI1_ImageData_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roi1_imagedata_rbv)
    
    def roi1_minx(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'roi1_minx' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ROI1_MinX' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roi1_minx)
    
    def roi1_minx_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'roi1_minx_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ROI1_MinX_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roi1_minx_rbv)
    
    def roi1_miny(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'roi1_miny' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ROI1_MinY' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roi1_miny)
    
    def roi1_miny_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'roi1_miny_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ROI1_MinY_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roi1_miny_rbv)
    
    def roi1_sizex(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'roi1_sizex' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ROI1_SizeX' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roi1_sizex)
    
    def roi1_sizex_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'roi1_sizex_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ROI1_SizeX_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roi1_sizex_rbv)
    
    def roi1_sizey(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'roi1_sizey' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ROI1_SizeY' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roi1_sizey)
    
    def roi1_sizey_rbv(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'roi1_sizey_rbv' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ROI1_SizeY_RBV' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roi1_sizey_rbv)
    
    def roiandmask_setx(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'roiandmask_setx' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ROIandMask_SetX' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roiandmask_setx)
    
    def roiandmask_setxrad(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'roiandmask_setxrad' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ROIandMask_SetXrad' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roiandmask_setxrad)
    
    def roiandmask_sety(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'roiandmask_sety' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ROIandMask_SetY' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roiandmask_sety)
    
    def roiandmask_setyrad(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'roiandmask_setyrad' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'ROIandMask_SetYrad' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.roiandmask_setyrad)
    
    def reset_buffer(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'reset_buffer' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'Reset_Buffer' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.reset_buffer)
    
    def save(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'save' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'Save' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.save)
    
    def save_buffer(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'save_buffer' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'Save_Buffer' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.save_buffer)
    
    def save_buffer_path_initialise(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'save_buffer_path_initialise' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'Save_Buffer_Path_Initialise' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.save_buffer_path_initialise)
    
    def save_path_initialise(self, name: Union[str, List[str], None] = None):
        """
        Returns the 'save_path_initialise' property of the camera(s).

        :param name: Name(s) of the camera.
        :type name: str or list of str or None

        :return: Value(s) of the 'Save_Path_Initialise' property.
        :rtype: property value or Dict[str, property value]
        """
        return self._get_property(name, property_=lambda camera: camera.save_path_initialise)
    