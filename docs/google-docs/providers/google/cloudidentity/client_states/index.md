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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>client_states</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>client_states</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudidentity.client_states" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the ClientState in format: `devices/{device}/deviceUsers/{device_user}/clientState/{partner}`, where partner corresponds to the partner storing the data. For partners belonging to the "BeyondCorp Alliance", this is the partner ID specified to you by Google. For all other callers, this is a string of the form: `{customer}-suffix`, where `customer` is your customer ID. The *suffix* is any string the caller specifies. This string will be displayed verbatim in the administration console. This suffix is used in setting up Custom Access Levels in Context-Aware Access. Your organization's customer ID can be obtained from the URL: `GET https://www.googleapis.com/admin/directory/v1/customers/my_customer` The `id` field in the response contains the customer ID starting with the letter 'C'. The customer ID to be used in this API is the string after the letter 'C' (not including 'C') |
| <CopyableCode code="assetTags" /> | `array` | The caller can specify asset tags for this resource |
| <CopyableCode code="complianceState" /> | `string` | The compliance state of the resource as specified by the API client. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the client state data was created. |
| <CopyableCode code="customId" /> | `string` | This field may be used to store a unique identifier for the API resource within which these CustomAttributes are a field. |
| <CopyableCode code="etag" /> | `string` | The token that needs to be passed back for concurrency control in updates. Token needs to be passed back in UpdateRequest |
| <CopyableCode code="healthScore" /> | `string` | The Health score of the resource. The Health score is the callers specification of the condition of the device from a usability point of view. For example, a third-party device management provider may specify a health score based on its compliance with organizational policies. |
| <CopyableCode code="keyValuePairs" /> | `object` | The map of key-value attributes stored by callers specific to a device. The total serialized length of this map may not exceed 10KB. No limit is placed on the number of attributes in a map. |
| <CopyableCode code="lastUpdateTime" /> | `string` | Output only. The time the client state data was last updated. |
| <CopyableCode code="managed" /> | `string` | The management state of the resource as specified by the API client. |
| <CopyableCode code="ownerType" /> | `string` | Output only. The owner of the ClientState |
| <CopyableCode code="scoreReason" /> | `string` | A descriptive cause of the health score. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clientStatesId, deviceUsersId, devicesId" /> | Gets the client state for the device user |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deviceUsersId, devicesId" /> | Lists the client states for the given search query. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="clientStatesId, deviceUsersId, devicesId" /> | Updates the client state for the device user **Note**: This method is available only to customers who have one of the following SKUs: Enterprise Standard, Enterprise Plus, Enterprise for Education, and Cloud Identity Premium |

## `SELECT` examples

Lists the client states for the given search query.

```sql
SELECT
name,
assetTags,
complianceState,
createTime,
customId,
etag,
healthScore,
keyValuePairs,
lastUpdateTime,
managed,
ownerType,
scoreReason
FROM google.cloudidentity.client_states
WHERE deviceUsersId = '{{ deviceUsersId }}'
AND devicesId = '{{ devicesId }}';
```

## `UPDATE` example

Updates a <code>client_states</code> resource.

```sql
/*+ update */
UPDATE google.cloudidentity.client_states
SET 
etag = '{{ etag }}',
customId = '{{ customId }}',
assetTags = '{{ assetTags }}',
healthScore = '{{ healthScore }}',
scoreReason = '{{ scoreReason }}',
managed = '{{ managed }}',
complianceState = '{{ complianceState }}',
keyValuePairs = '{{ keyValuePairs }}'
WHERE 
clientStatesId = '{{ clientStatesId }}'
AND deviceUsersId = '{{ deviceUsersId }}'
AND devicesId = '{{ devicesId }}';
```
