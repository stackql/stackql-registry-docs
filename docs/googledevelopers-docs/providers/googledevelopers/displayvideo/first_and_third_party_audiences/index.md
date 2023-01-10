---
title: first_and_third_party_audiences
hide_title: false
hide_table_of_contents: false
keywords:
  - first_and_third_party_audiences
  - displayvideo
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>first_and_third_party_audiences</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.first_and_third_party_audiences</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the first and third party audience. |
| `description` | `string` | The user-provided description of the audience. Only applicable to first party audiences. |
| `firstAndThirdPartyAudienceId` | `string` | Output only. The unique ID of the first and third party audience. Assigned by the system. |
| `membershipDurationDays` | `string` | The duration in days that an entry remains in the audience after the qualifying event. If the audience has no expiration, set the value of this field to 10000. Otherwise, the set value must be greater than 0 and less than or equal to 540. Only applicable to first party audiences. This field is required if one of the following audience_type is used: * `CUSTOMER_MATCH_CONTACT_INFO` * `CUSTOMER_MATCH_DEVICE_ID` |
| `displayDesktopAudienceSize` | `string` | Output only. The estimated desktop audience size in Display network. If the size is less than 1000, the number will be hidden and 0 will be returned due to privacy reasons. Otherwise, the number will be rounded off to two significant digits. Only applicable to first party audiences. Only returned in GET request. |
| `gmailAudienceSize` | `string` | Output only. The estimated audience size for Gmail network. If the size is less than 1000, the number will be hidden and 0 will be returned due to privacy reasons. Otherwise, the number will be rounded off to two significant digits. Only applicable to first party audiences. Only returned in GET request. |
| `displayMobileWebAudienceSize` | `string` | Output only. The estimated mobile web audience size in Display network. If the size is less than 1000, the number will be hidden and 0 will be returned due to privacy reasons. Otherwise, the number will be rounded off to two significant digits. Only applicable to first party audiences. Only returned in GET request. |
| `contactInfoList` | `object` | Wrapper message for a list of contact information defining Customer Match audience members. |
| `mobileDeviceIdList` | `object` | Wrapper message for a list of mobile device IDs defining Customer Match audience members. |
| `youtubeAudienceSize` | `string` | Output only. The estimated audience size for YouTube network. If the size is less than 1000, the number will be hidden and 0 will be returned due to privacy reasons. Otherwise, the number will be rounded off to two significant digits. Only applicable to first party audiences. Only returned in GET request. |
| `displayName` | `string` | The display name of the first and third party audience. |
| `appId` | `string` | The app_id matches with the type of the mobile_device_ids being uploaded. Only applicable to audience_type `CUSTOMER_MATCH_DEVICE_ID` |
| `audienceSource` | `string` | Output only. The source of the audience. |
| `displayAudienceSize` | `string` | Output only. The estimated audience size for the Display network. If the size is less than 1000, the number will be hidden and 0 will be returned due to privacy reasons. Otherwise, the number will be rounded off to two significant digits. Only returned in GET request. |
| `firstAndThirdPartyAudienceType` | `string` | Whether the audience is a first or third party audience. |
| `audienceType` | `string` | The type of the audience. |
| `displayMobileAppAudienceSize` | `string` | Output only. The estimated mobile app audience size in Display network. If the size is less than 1000, the number will be hidden and 0 will be returned due to privacy reasons. Otherwise, the number will be rounded off to two significant digits. Only applicable to first party audiences. Only returned in GET request. |
| `activeDisplayAudienceSize` | `string` | Output only. The estimated audience size for the Display network in the past month. If the size is less than 1000, the number will be hidden and 0 will be returned due to privacy reasons. Otherwise, the number will be rounded off to two significant digits. Only returned in GET request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `firstAndThirdPartyAudiences_get` | `SELECT` | `firstAndThirdPartyAudiencesId` | Gets a first and third party audience. |
| `firstAndThirdPartyAudiences_list` | `SELECT` |  | Lists first and third party audiences. The order is defined by the order_by parameter. |
| `firstAndThirdPartyAudiences_create` | `INSERT` |  | Creates a FirstAndThirdPartyAudience. Only supported for the following audience_type: * `CUSTOMER_MATCH_CONTACT_INFO` * `CUSTOMER_MATCH_DEVICE_ID` |
| `firstAndThirdPartyAudiences_editCustomerMatchMembers` | `EXEC` | `firstAndThirdPartyAudiencesId` | Updates the member list of a Customer Match audience. Only supported for the following audience_type: * `CUSTOMER_MATCH_CONTACT_INFO` * `CUSTOMER_MATCH_DEVICE_ID` |
| `firstAndThirdPartyAudiences_patch` | `EXEC` | `firstAndThirdPartyAudiencesId` | Updates an existing FirstAndThirdPartyAudience. Only supported for the following audience_type: * `CUSTOMER_MATCH_CONTACT_INFO` * `CUSTOMER_MATCH_DEVICE_ID` |
