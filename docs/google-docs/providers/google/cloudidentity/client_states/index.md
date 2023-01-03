---
title: client_states
hide_title: false
hide_table_of_contents: false
keywords:
  - client_states
  - cloudidentity
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>client_states</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudidentity.client_states</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the ClientState in format: `devices/{device}/deviceUsers/{device_user}/clientState/{partner}`, where partner corresponds to the partner storing the data. For partners belonging to the "BeyondCorp Alliance", this is the partner ID specified to you by Google. For all other callers, this is a string of the form: `{customer}-suffix`, where `customer` is your customer ID. The *suffix* is any string the caller specifies. This string will be displayed verbatim in the administration console. This suffix is used in setting up Custom Access Levels in Context-Aware Access. Your organization's customer ID can be obtained from the URL: `GET https://www.googleapis.com/admin/directory/v1/customers/my_customer` The `id` field in the response contains the customer ID starting with the letter 'C'. The customer ID to be used in this API is the string after the letter 'C' (not including 'C') |
| `assetTags` | `array` | The caller can specify asset tags for this resource |
| `ownerType` | `string` | Output only. The owner of the ClientState |
| `etag` | `string` | The token that needs to be passed back for concurrency control in updates. Token needs to be passed back in UpdateRequest |
| `lastUpdateTime` | `string` | Output only. The time the client state data was last updated. |
| `managed` | `string` | The management state of the resource as specified by the API client. |
| `healthScore` | `string` | The Health score of the resource. The Health score is the callers specification of the condition of the device from a usability point of view. For example, a third-party device management provider may specify a health score based on its compliance with organizational policies. |
| `keyValuePairs` | `object` | The map of key-value attributes stored by callers specific to a device. The total serialized length of this map may not exceed 10KB. No limit is placed on the number of attributes in a map. |
| `scoreReason` | `string` | A descriptive cause of the health score. |
| `createTime` | `string` | Output only. The time the client state data was created. |
| `complianceState` | `string` | The compliance state of the resource as specified by the API client. |
| `customId` | `string` | This field may be used to store a unique identifier for the API resource within which these CustomAttributes are a field. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `devices_deviceUsers_clientStates_get` | `SELECT` | `clientStatesId, deviceUsersId, devicesId` | Gets the client state for the device user |
| `devices_deviceUsers_clientStates_list` | `SELECT` | `deviceUsersId, devicesId` | Lists the client states for the given search query. |
| `devices_deviceUsers_clientStates_patch` | `EXEC` | `clientStatesId, deviceUsersId, devicesId` | Updates the client state for the device user **Note**: This method is available only to customers who have one of the following SKUs: Enterprise Standard, Enterprise Plus, Enterprise for Education, and Cloud Identity Premium |
