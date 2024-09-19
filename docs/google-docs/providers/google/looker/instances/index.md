---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - looker
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.looker.instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Format: `projects/{project}/locations/{location}/instances/{instance}`. |
| <CopyableCode code="adminSettings" /> | `object` | Looker instance Admin settings fields. |
| <CopyableCode code="consumerNetwork" /> | `string` | Network name in the consumer project. Format: `projects/{project}/global/networks/{network}`. Note that the consumer network may be in a different GCP project than the consumer project that is hosting the Looker Instance. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the Looker instance provisioning was first requested. |
| <CopyableCode code="customDomain" /> | `object` | Custom domain information. |
| <CopyableCode code="denyMaintenancePeriod" /> | `object` | Specifies the maintenance denial period. |
| <CopyableCode code="egressPublicIp" /> | `string` | Output only. Public Egress IP (IPv4). |
| <CopyableCode code="encryptionConfig" /> | `object` | Encryption configuration (i.e. CMEK). |
| <CopyableCode code="fipsEnabled" /> | `boolean` | Optional. Whether FIPS is enabled on the Looker instance. |
| <CopyableCode code="geminiEnabled" /> | `boolean` | Optional. Whether Gemini feature is enabled on the Looker instance or not. |
| <CopyableCode code="ingressPrivateIp" /> | `string` | Output only. Private Ingress IP (IPv4). |
| <CopyableCode code="ingressPublicIp" /> | `string` | Output only. Public Ingress IP (IPv4). |
| <CopyableCode code="lastDenyMaintenancePeriod" /> | `object` | Specifies the maintenance denial period. |
| <CopyableCode code="linkedLspProjectNumber" /> | `string` | Optional. Linked Google Cloud Project Number for Looker Studio Pro. |
| <CopyableCode code="lookerUri" /> | `string` | Output only. Looker instance URI which can be used to access the Looker Instance UI. |
| <CopyableCode code="lookerVersion" /> | `string` | Output only. The Looker version that the instance is using. |
| <CopyableCode code="maintenanceSchedule" /> | `object` | Published upcoming future maintenance schedule. |
| <CopyableCode code="maintenanceWindow" /> | `object` | Specifies the recurring maintenance window. |
| <CopyableCode code="oauthConfig" /> | `object` | Looker instance OAuth login settings. |
| <CopyableCode code="platformEdition" /> | `string` | Platform edition. |
| <CopyableCode code="privateIpEnabled" /> | `boolean` | Whether private IP is enabled on the Looker instance. |
| <CopyableCode code="pscConfig" /> | `object` | Information for Private Service Connect (PSC) setup for a Looker instance. |
| <CopyableCode code="pscEnabled" /> | `boolean` | Optional. Whether to use Private Service Connect (PSC) for private IP connectivity. If true, neither `public_ip_enabled` nor `private_ip_enabled` can be true. |
| <CopyableCode code="publicIpEnabled" /> | `boolean` | Whether public IP is enabled on the Looker instance. |
| <CopyableCode code="reservedRange" /> | `string` | Name of a reserved IP address range within the Instance.consumer_network, to be used for private services access connection. May or may not be specified in a create request. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the instance. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the Looker instance was last updated. |
| <CopyableCode code="userMetadata" /> | `object` | Metadata about users for a Looker instance. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Gets details of a single Instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Instances in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Instance in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Delete instance. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Update Instance. |
| <CopyableCode code="export" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Export instance. |
| <CopyableCode code="import" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Import instance. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Restart instance. |

## `SELECT` examples

Lists Instances in a given project and location.

```sql
SELECT
name,
adminSettings,
consumerNetwork,
createTime,
customDomain,
denyMaintenancePeriod,
egressPublicIp,
encryptionConfig,
fipsEnabled,
geminiEnabled,
ingressPrivateIp,
ingressPublicIp,
lastDenyMaintenancePeriod,
linkedLspProjectNumber,
lookerUri,
lookerVersion,
maintenanceSchedule,
maintenanceWindow,
oauthConfig,
platformEdition,
privateIpEnabled,
pscConfig,
pscEnabled,
publicIpEnabled,
reservedRange,
state,
updateTime,
userMetadata
FROM google.looker.instances
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
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
INSERT INTO google.looker.instances (
locationsId,
projectsId,
platformEdition,
publicIpEnabled,
privateIpEnabled,
pscEnabled,
pscConfig,
consumerNetwork,
reservedRange,
maintenanceWindow,
denyMaintenancePeriod,
maintenanceSchedule,
userMetadata,
customDomain,
encryptionConfig,
adminSettings,
oauthConfig,
linkedLspProjectNumber,
fipsEnabled,
geminiEnabled
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ platformEdition }}',
true|false,
true|false,
true|false,
'{{ pscConfig }}',
'{{ consumerNetwork }}',
'{{ reservedRange }}',
'{{ maintenanceWindow }}',
'{{ denyMaintenancePeriod }}',
'{{ maintenanceSchedule }}',
'{{ userMetadata }}',
'{{ customDomain }}',
'{{ encryptionConfig }}',
'{{ adminSettings }}',
'{{ oauthConfig }}',
'{{ linkedLspProjectNumber }}',
true|false,
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
createTime: string
updateTime: string
state: string
platformEdition: string
publicIpEnabled: boolean
privateIpEnabled: boolean
lookerVersion: string
egressPublicIp: string
ingressPrivateIp: string
ingressPublicIp: string
lookerUri: string
pscEnabled: boolean
pscConfig:
  allowedVpcs:
    - type: string
  serviceAttachments:
    - localFqdn: string
      targetServiceAttachmentUri: string
      connectionStatus: string
  lookerServiceAttachmentUri: string
consumerNetwork: string
reservedRange: string
maintenanceWindow:
  dayOfWeek: string
  startTime:
    hours: integer
    minutes: integer
    seconds: integer
    nanos: integer
denyMaintenancePeriod:
  startDate:
    year: integer
    month: integer
    day: integer
maintenanceSchedule:
  startTime: string
  endTime: string
userMetadata:
  additionalViewerUserCount: integer
  additionalStandardUserCount: integer
  additionalDeveloperUserCount: integer
customDomain:
  domain: string
  state: string
encryptionConfig:
  kmsKeyName: string
  kmsKeyState: string
  kmsKeyNameVersion: string
adminSettings:
  allowedEmailDomains:
    - type: string
oauthConfig:
  clientId: string
  clientSecret: string
linkedLspProjectNumber: string
fipsEnabled: boolean
geminiEnabled: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>instances</code> resource.

```sql
/*+ update */
UPDATE google.looker.instances
SET 
platformEdition = '{{ platformEdition }}',
publicIpEnabled = true|false,
privateIpEnabled = true|false,
pscEnabled = true|false,
pscConfig = '{{ pscConfig }}',
consumerNetwork = '{{ consumerNetwork }}',
reservedRange = '{{ reservedRange }}',
maintenanceWindow = '{{ maintenanceWindow }}',
denyMaintenancePeriod = '{{ denyMaintenancePeriod }}',
maintenanceSchedule = '{{ maintenanceSchedule }}',
userMetadata = '{{ userMetadata }}',
customDomain = '{{ customDomain }}',
encryptionConfig = '{{ encryptionConfig }}',
adminSettings = '{{ adminSettings }}',
oauthConfig = '{{ oauthConfig }}',
linkedLspProjectNumber = '{{ linkedLspProjectNumber }}',
fipsEnabled = true|false,
geminiEnabled = true|false
WHERE 
instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>instances</code> resource.

```sql
/*+ delete */
DELETE FROM google.looker.instances
WHERE instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
