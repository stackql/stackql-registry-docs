---
title: creatives
hide_title: false
hide_table_of_contents: false
keywords:
  - creatives
  - dfareporting
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>creatives</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.creatives</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this creative. This is a read-only, auto-generated field. Applicable to all creative types. |
| `name` | `string` | Name of the creative. This is a required field and must be less than 256 characters long. Applicable to all creative types. |
| `requiredFlashPluginVersion` | `string` | The minimum required Flash plugin version for this creative. For example, 11.2.202.235. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. |
| `renderingIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `mediaDuration` | `number` | Creative audio or video duration in seconds. This is a read-only field. Applicable to the following creative types: INSTREAM_VIDEO, INSTREAM_AUDIO, all RICH_MEDIA, and all VPAID. |
| `counterCustomEvents` | `array` | List of counter events configured for the creative. For DISPLAY_IMAGE_GALLERY creatives, these are read-only and auto-generated from clickTags. Applicable to the following creative types: DISPLAY_IMAGE_GALLERY, all RICH_MEDIA, and all VPAID. |
| `sslOverride` | `boolean` | Whether creative should be treated as SSL compliant even if the system scan shows it's not. Applicable to all creative types. |
| `dynamicAssetSelection` | `boolean` | Set this to true to enable the use of rules to target individual assets in this creative. When set to true creativeAssetSelection must be set. This also controls asset-level companions. When this is true, companion creatives should be assigned to creative assets. Learn more. Applicable to INSTREAM_VIDEO creatives. |
| `version` | `integer` | The version number helps you keep track of multiple versions of your creative in your reports. The version number will always be auto-generated during insert operations to start at 1. For tracking creatives the version cannot be incremented and will always remain at 1. For all other creative types the version can be incremented only by 1 during update operations. In addition, the version will be automatically incremented by 1 when undergoing Rich Media creative merging. Applicable to all creative types. |
| `companionCreatives` | `array` | List of companion creatives assigned to an in-Stream video creative. Acceptable values include IDs of existing flash and image creatives. Applicable to the following creative types: all VPAID, all INSTREAM_AUDIO and all INSTREAM_VIDEO with dynamicAssetSelection set to false. |
| `adParameters` | `string` | Ad parameters user for VPAID creative. This is a read-only field. Applicable to the following creative types: all VPAID. |
| `backupImageFeatures` | `array` | List of feature dependencies that will cause a backup image to be served if the browser that serves the ad does not support them. Feature dependencies are features that a browser must be able to support in order to render your HTML5 creative asset correctly. This field is initially auto-generated to contain all features detected by Campaign Manager for all the assets of this creative and can then be modified by the client. To reset this field, copy over all the creativeAssets' detected features. Applicable to the following creative types: HTML5_BANNER. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE. |
| `size` | `object` | Represents the dimensions of ads, placements, creatives, or creative assets. |
| `obaIcon` | `object` | Online Behavioral Advertiser icon. |
| `totalFileSize` | `string` | Combined size of all creative assets. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. |
| `skipOffset` | `object` | Video Offset |
| `skippable` | `boolean` | Whether the user can choose to skip the creative. Applicable to the following creative types: all INSTREAM_VIDEO and all VPAID. |
| `creativeFieldAssignments` | `array` | Creative field assignments for this creative. Applicable to all creative types. |
| `requiredFlashVersion` | `integer` | The internal Flash version for this creative as calculated by Studio. This is a read-only field. Applicable to the following creative types: FLASH_INPAGE all RICH_MEDIA, and all VPAID. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE. |
| `progressOffset` | `object` | Video Offset |
| `advertiserId` | `string` | Advertiser ID of this creative. This is a required field. Applicable to all creative types. |
| `thirdPartyRichMediaImpressionsUrl` | `string` | Third-party URL used to record rich media impressions. Applicable to the following creative types: all RICH_MEDIA. |
| `backupImageReportingLabel` | `string` | Reporting label used for HTML5 banner backup image. Applicable to the following creative types: DISPLAY when the primary asset type is not HTML_IMAGE. |
| `type` | `string` | Type of this creative. This is a required field. Applicable to all creative types. *Note:* FLASH_INPAGE, HTML5_BANNER, and IMAGE are only used for existing creatives. New creatives should use DISPLAY as a replacement for these types. |
| `creativeAssets` | `array` | Assets associated with a creative. Applicable to all but the following creative types: INTERNAL_REDIRECT, INTERSTITIAL_INTERNAL_REDIRECT, and REDIRECT |
| `adTagKeys` | `array` | Keywords for a Rich Media creative. Keywords let you customize the creative settings of a Rich Media ad running on your site without having to contact the advertiser. You can use keywords to dynamically change the look or functionality of a creative. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. |
| `authoringTool` | `string` | Authoring tool for HTML5 banner creatives. This is a read-only field. Applicable to the following creative types: HTML5_BANNER. |
| `studioTraffickedCreativeId` | `string` | Studio trafficked creative ID associated with rich media and VPAID creatives. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. |
| `timerCustomEvents` | `array` | List of timer events configured for the creative. For DISPLAY_IMAGE_GALLERY creatives, these are read-only and auto-generated from clickTags. Applicable to the following creative types: DISPLAY_IMAGE_GALLERY, all RICH_MEDIA, and all VPAID. Applicable to DISPLAY when the primary asset is not HTML_IMAGE. |
| `backupImageTargetWindow` | `object` | Target Window. |
| `autoAdvanceImages` | `boolean` | Whether images are automatically advanced for image gallery creatives. Applicable to the following creative types: DISPLAY_IMAGE_GALLERY. |
| `convertFlashToHtml5` | `boolean` | Whether Flash assets associated with the creative need to be automatically converted to HTML5. This flag is enabled by default and users can choose to disable it if they don't want the system to generate and use HTML5 asset for this creative. Applicable to the following creative type: FLASH_INPAGE. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE. |
| `lastModifiedInfo` | `object` | Modification timestamp. |
| `commercialId` | `string` | Industry standard ID assigned to creative for reach and frequency. Applicable to INSTREAM_VIDEO_REDIRECT creatives. |
| `redirectUrl` | `string` | URL of hosted image or hosted video or another ad tag. For INSTREAM_VIDEO_REDIRECT creatives this is the in-stream video redirect URL. The standard for a VAST (Video Ad Serving Template) ad response allows for a redirect link to another VAST 2.0 or 3.0 call. This is a required field when applicable. Applicable to the following creative types: DISPLAY_REDIRECT, INTERNAL_REDIRECT, INTERSTITIAL_INTERNAL_REDIRECT, and INSTREAM_VIDEO_REDIRECT |
| `archived` | `boolean` | Whether the creative is archived. Applicable to all creative types. |
| `customKeyValues` | `array` | Custom key-values for a Rich Media creative. Key-values let you customize the creative settings of a Rich Media ad running on your site without having to contact the advertiser. You can use key-values to dynamically change the look or functionality of a creative. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. |
| `thirdPartyUrls` | `array` | Third-party URLs for tracking in-stream creative events. Applicable to the following creative types: all INSTREAM_VIDEO, all INSTREAM_AUDIO, and all VPAID. |
| `htmlCodeLocked` | `boolean` | Whether HTML code is generated by Campaign Manager or manually entered. Set to true to ignore changes to htmlCode. Applicable to the following creative types: FLASH_INPAGE and HTML5_BANNER. |
| `subaccountId` | `string` | Subaccount ID of this creative. This field, if left unset, will be auto-generated for both insert and update operations. Applicable to all creative types. |
| `creativeAssetSelection` | `object` | Encapsulates the list of rules for asset selection and a default asset in case none of the rules match. Applicable to INSTREAM_VIDEO creatives. |
| `allowScriptAccess` | `boolean` | Whether script access is allowed for this creative. This is a read-only and deprecated field which will automatically be set to true on update. Applicable to the following creative types: FLASH_INPAGE. |
| `fsCommand` | `object` | FsCommand. |
| `universalAdId` | `object` | A Universal Ad ID as per the VAST 4.0 spec. Applicable to the following creative types: INSTREAM_AUDIO, INSTREAM_VIDEO and VPAID. |
| `clickTags` | `array` | Click tags of the creative. For DISPLAY, FLASH_INPAGE, and HTML5_BANNER creatives, this is a subset of detected click tags for the assets associated with this creative. After creating a flash asset, detected click tags will be returned in the creativeAssetMetadata. When inserting the creative, populate the creative clickTags field using the creativeAssetMetadata.clickTags field. For DISPLAY_IMAGE_GALLERY creatives, there should be exactly one entry in this list for each image creative asset. A click tag is matched with a corresponding creative asset by matching the clickTag.name field with the creativeAsset.assetIdentifier.name field. Applicable to the following creative types: DISPLAY_IMAGE_GALLERY, FLASH_INPAGE, HTML5_BANNER. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE. |
| `artworkType` | `string` | Type of artwork used for the creative. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. |
| `htmlCode` | `string` | HTML code for the creative. This is a required field when applicable. This field is ignored if htmlCodeLocked is true. Applicable to the following creative types: all CUSTOM, FLASH_INPAGE, and HTML5_BANNER, and all RICH_MEDIA. |
| `compatibility` | `array` | Compatibilities associated with this creative. This is a read-only field. DISPLAY and DISPLAY_INTERSTITIAL refer to rendering either on desktop or on mobile devices or in mobile apps for regular or interstitial ads, respectively. APP and APP_INTERSTITIAL are for rendering in mobile apps. Only pre-existing creatives may have these compatibilities since new creatives will either be assigned DISPLAY or DISPLAY_INTERSTITIAL instead. IN_STREAM_VIDEO refers to rendering in in-stream video ads developed with the VAST standard. IN_STREAM_AUDIO refers to rendering in in-stream audio ads developed with the VAST standard. Applicable to all creative types. Acceptable values are: - "APP" - "APP_INTERSTITIAL" - "IN_STREAM_VIDEO" - "IN_STREAM_AUDIO" - "DISPLAY" - "DISPLAY_INTERSTITIAL"  |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#creative". |
| `idDimensionValue` | `object` | Represents a DimensionValue resource. |
| `backgroundColor` | `string` | The 6-character HTML color code, beginning with #, for the background of the window area where the Flash file is displayed. Default is white. Applicable to the following creative types: FLASH_INPAGE. |
| `additionalSizes` | `array` | Additional sizes associated with a responsive creative. When inserting or updating a creative either the size ID field or size width and height fields can be used. Applicable to DISPLAY creatives when the primary asset type is HTML_IMAGE. |
| `accountId` | `string` | Account ID of this creative. This field, if left unset, will be auto-generated for both insert and update operations. Applicable to all creative types. |
| `studioCreativeId` | `string` | Studio creative ID associated with rich media and VPAID creatives. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. |
| `thirdPartyBackupImageImpressionsUrl` | `string` | Third-party URL used to record backup image impressions. Applicable to the following creative types: all RICH_MEDIA. |
| `authoringSource` | `string` | Source application where creative was authored. Presently, only DBM authored creatives will have this field set. Applicable to all creative types. |
| `exitCustomEvents` | `array` | List of exit events configured for the creative. For DISPLAY and DISPLAY_IMAGE_GALLERY creatives, these are read-only and auto-generated from clickTags, For DISPLAY, an event is also created from the backupImageReportingLabel. Applicable to the following creative types: DISPLAY_IMAGE_GALLERY, all RICH_MEDIA, and all VPAID. Applicable to DISPLAY when the primary asset type is not HTML_IMAGE. |
| `mediaDescription` | `string` | Description of the audio or video ad. Applicable to the following creative types: all INSTREAM_VIDEO, INSTREAM_AUDIO, and all VPAID. |
| `overrideCss` | `string` | Override CSS value for rich media creatives. Applicable to the following creative types: all RICH_MEDIA. |
| `backupImageClickThroughUrl` | `object` | Click-through URL |
| `active` | `boolean` | Whether the creative is active. Applicable to all creative types. |
| `sslCompliant` | `boolean` | Whether the creative is SSL-compliant. This is a read-only field. Applicable to all creative types. |
| `studioAdvertiserId` | `string` | Studio advertiser ID associated with rich media and VPAID creatives. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. |
| `latestTraffickedCreativeId` | `string` | Latest Studio trafficked creative ID associated with rich media and VPAID creatives. This is a read-only field. Applicable to the following creative types: all RICH_MEDIA, and all VPAID. |
| `renderingId` | `string` | ID of current rendering version. This is a read-only field. Applicable to all creative types. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `id, profileId` | Gets one creative by ID. |
| `list` | `SELECT` | `profileId` | Retrieves a list of creatives, possibly filtered. This method supports paging. |
| `insert` | `INSERT` | `profileId` | Inserts a new creative. |
| `patch` | `EXEC` | `id, profileId` | Updates an existing creative. This method supports patch semantics. |
| `update` | `EXEC` | `profileId` | Updates an existing creative. |
