---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - apigee
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

Creates, updates, deletes, gets or lists a <code>instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Resource ID of the instance. Values must match the regular expression `^a-z{0,30}[a-z\d]$`. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the instance. |
| <CopyableCode code="accessLoggingConfig" /> | `object` | Access logging configuration enables customers to ship the access logs from the tenant projects to their own project's cloud logging. The feature is at the instance level ad disabled by default. It can be enabled during CreateInstance or UpdateInstance. |
| <CopyableCode code="consumerAcceptList" /> | `array` | Optional. Customer accept list represents the list of projects (id/number) on customer side that can privately connect to the service attachment. It is an optional field which the customers can provide during the instance creation. By default, the customer project associated with the Apigee organization will be included to the list. |
| <CopyableCode code="createdAt" /> | `string` | Output only. Time the instance was created in milliseconds since epoch. |
| <CopyableCode code="diskEncryptionKeyName" /> | `string` | Customer Managed Encryption Key (CMEK) used for disk and volume encryption. If not specified, a Google-Managed encryption key will be used. Use the following format: `projects/([^/]+)/locations/([^/]+)/keyRings/([^/]+)/cryptoKeys/([^/]+)` |
| <CopyableCode code="displayName" /> | `string` | Optional. Display name for the instance. |
| <CopyableCode code="host" /> | `string` | Output only. Internal hostname or IP address of the Apigee endpoint used by clients to connect to the service. |
| <CopyableCode code="ipRange" /> | `string` | Optional. Comma-separated list of CIDR blocks of length 22 and/or 28 used to create the Apigee instance. Providing CIDR ranges is optional. You can provide just /22 or /28 or both (or neither). Ranges you provide should be freely available as part of a larger named range you have allocated to the Service Networking peering. If this parameter is not provided, Apigee automatically requests an available /22 and /28 CIDR block from Service Networking. Use the /22 CIDR block for configuring your firewall needs to allow traffic from Apigee. Input formats: `a.b.c.d/22` or `e.f.g.h/28` or `a.b.c.d/22,e.f.g.h/28` |
| <CopyableCode code="lastModifiedAt" /> | `string` | Output only. Time the instance was last modified in milliseconds since epoch. |
| <CopyableCode code="location" /> | `string` | Required. Compute Engine location where the instance resides. |
| <CopyableCode code="peeringCidrRange" /> | `string` | Optional. Size of the CIDR block range that will be reserved by the instance. PAID organizations support `SLASH_16` to `SLASH_20` and defaults to `SLASH_16`. Evaluation organizations support only `SLASH_23`. |
| <CopyableCode code="port" /> | `string` | Output only. Port number of the exposed Apigee endpoint. |
| <CopyableCode code="runtimeVersion" /> | `string` | Output only. Version of the runtime system running in the instance. The runtime system is the set of components that serve the API Proxy traffic in your Environments. |
| <CopyableCode code="serviceAttachment" /> | `string` | Output only. Resource name of the service attachment created for the instance in the format: `projects/*/regions/*/serviceAttachments/*` Apigee customers can privately forward traffic to this service attachment using the PSC endpoints. |
| <CopyableCode code="state" /> | `string` | Output only. State of the instance. Values other than `ACTIVE` means the resource is not ready to use. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_instances_get" /> | `SELECT` | <CopyableCode code="instancesId, organizationsId" /> | Gets the details for an Apigee runtime instance. **Note:** Not supported for Apigee hybrid. |
| <CopyableCode code="organizations_instances_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists all Apigee runtime instances for the organization. **Note:** Not supported for Apigee hybrid. |
| <CopyableCode code="organizations_instances_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates an Apigee runtime instance. The instance is accessible from the authorized network configured on the organization. **Note:** Not supported for Apigee hybrid. |
| <CopyableCode code="organizations_instances_delete" /> | `DELETE` | <CopyableCode code="instancesId, organizationsId" /> | Deletes an Apigee runtime instance. The instance stops serving requests and the runtime data is deleted. **Note:** Not supported for Apigee hybrid. |
| <CopyableCode code="organizations_instances_patch" /> | `UPDATE` | <CopyableCode code="instancesId, organizationsId" /> | Updates an Apigee runtime instance. You can update the fields described in NodeConfig. No other fields will be updated. **Note:** Not supported for Apigee hybrid. |
| <CopyableCode code="organizations_instances_report_status" /> | `EXEC` | <CopyableCode code="instancesId, organizationsId" /> | Reports the latest status for a runtime instance. |

## `SELECT` examples

Lists all Apigee runtime instances for the organization. **Note:** Not supported for Apigee hybrid.

```sql
SELECT
name,
description,
accessLoggingConfig,
consumerAcceptList,
createdAt,
diskEncryptionKeyName,
displayName,
host,
ipRange,
lastModifiedAt,
location,
peeringCidrRange,
port,
runtimeVersion,
serviceAttachment,
state
FROM google.apigee.instances
WHERE organizationsId = '{{ organizationsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instances</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.apigee.instances (
organizationsId,
serviceAttachment,
runtimeVersion,
accessLoggingConfig,
ipRange,
host,
lastModifiedAt,
name,
displayName,
description,
location,
peeringCidrRange,
port,
diskEncryptionKeyName,
state,
consumerAcceptList,
createdAt
)
SELECT 
'{{ organizationsId }}',
'{{ serviceAttachment }}',
'{{ runtimeVersion }}',
'{{ accessLoggingConfig }}',
'{{ ipRange }}',
'{{ host }}',
'{{ lastModifiedAt }}',
'{{ name }}',
'{{ displayName }}',
'{{ description }}',
'{{ location }}',
'{{ peeringCidrRange }}',
'{{ port }}',
'{{ diskEncryptionKeyName }}',
'{{ state }}',
'{{ consumerAcceptList }}',
'{{ createdAt }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: serviceAttachment
      value: '{{ serviceAttachment }}'
    - name: runtimeVersion
      value: '{{ runtimeVersion }}'
    - name: accessLoggingConfig
      value: '{{ accessLoggingConfig }}'
    - name: ipRange
      value: '{{ ipRange }}'
    - name: host
      value: '{{ host }}'
    - name: lastModifiedAt
      value: '{{ lastModifiedAt }}'
    - name: name
      value: '{{ name }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: description
      value: '{{ description }}'
    - name: location
      value: '{{ location }}'
    - name: peeringCidrRange
      value: '{{ peeringCidrRange }}'
    - name: port
      value: '{{ port }}'
    - name: diskEncryptionKeyName
      value: '{{ diskEncryptionKeyName }}'
    - name: state
      value: '{{ state }}'
    - name: consumerAcceptList
      value: '{{ consumerAcceptList }}'
    - name: createdAt
      value: '{{ createdAt }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>instances</code> resource.

```sql
/*+ update */
UPDATE google.apigee.instances
SET 
serviceAttachment = '{{ serviceAttachment }}',
runtimeVersion = '{{ runtimeVersion }}',
accessLoggingConfig = '{{ accessLoggingConfig }}',
ipRange = '{{ ipRange }}',
host = '{{ host }}',
lastModifiedAt = '{{ lastModifiedAt }}',
name = '{{ name }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
location = '{{ location }}',
peeringCidrRange = '{{ peeringCidrRange }}',
port = '{{ port }}',
diskEncryptionKeyName = '{{ diskEncryptionKeyName }}',
state = '{{ state }}',
consumerAcceptList = '{{ consumerAcceptList }}',
createdAt = '{{ createdAt }}'
WHERE 
instancesId = '{{ instancesId }}'
AND organizationsId = '{{ organizationsId }}';
```

## `DELETE` example

Deletes the specified <code>instances</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigee.instances
WHERE instancesId = '{{ instancesId }}'
AND organizationsId = '{{ organizationsId }}';
```
