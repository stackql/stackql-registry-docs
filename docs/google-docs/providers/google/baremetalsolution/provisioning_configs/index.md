
---
title: provisioning_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - provisioning_configs
  - baremetalsolution
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

Creates, updates, deletes or gets an <code>provisioning_config</code> resource or lists <code>provisioning_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provisioning_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.baremetalsolution.provisioning_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The system-generated name of the provisioning config. This follows the UUID format. |
| <CopyableCode code="cloudConsoleUri" /> | `string` | Output only. URI to Cloud Console UI view of this provisioning config. |
| <CopyableCode code="customId" /> | `string` | Optional. The user-defined identifier of the provisioning config. |
| <CopyableCode code="email" /> | `string` | Email provided to send a confirmation with provisioning config to. Deprecated in favour of email field in request messages. |
| <CopyableCode code="handoverServiceAccount" /> | `string` | A service account to enable customers to access instance credentials upon handover. |
| <CopyableCode code="instances" /> | `array` | Instances to be created. |
| <CopyableCode code="location" /> | `string` | Optional. Location name of this ProvisioningConfig. It is optional only for Intake UI transition period. |
| <CopyableCode code="networks" /> | `array` | Networks to be created. |
| <CopyableCode code="pod" /> | `string` | Optional. Pod name. Pod is an independent part of infrastructure. Instance can be connected to the assets (networks, volumes, nfsshares) allocated in the same pod only. |
| <CopyableCode code="state" /> | `string` | Output only. State of ProvisioningConfig. |
| <CopyableCode code="statusMessage" /> | `string` | Optional status messages associated with the FAILED state. |
| <CopyableCode code="ticketId" /> | `string` | A generated ticket id to track provisioning request. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update timestamp. |
| <CopyableCode code="volumes" /> | `array` | Volumes to be created. |
| <CopyableCode code="vpcScEnabled" /> | `boolean` | If true, VPC SC is enabled for the cluster. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, provisioningConfigsId" /> | Get ProvisioningConfig by name. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create new ProvisioningConfig. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, provisioningConfigsId" /> | Update existing ProvisioningConfig. |
| <CopyableCode code="submit" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Submit a provisiong configuration for a given project. |

## `SELECT` examples

Get ProvisioningConfig by name.

```sql
SELECT
name,
cloudConsoleUri,
customId,
email,
handoverServiceAccount,
instances,
location,
networks,
pod,
state,
statusMessage,
ticketId,
updateTime,
volumes,
vpcScEnabled
FROM google.baremetalsolution.provisioning_configs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND provisioningConfigsId = '{{ provisioningConfigsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>provisioning_configs</code> resource.

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
INSERT INTO google.baremetalsolution.provisioning_configs (
locationsId,
projectsId,
name,
instances,
networks,
volumes,
ticketId,
handoverServiceAccount,
email,
state,
location,
updateTime,
cloudConsoleUri,
vpcScEnabled,
statusMessage,
customId,
pod
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ instances }}',
'{{ networks }}',
'{{ volumes }}',
'{{ ticketId }}',
'{{ handoverServiceAccount }}',
'{{ email }}',
'{{ state }}',
'{{ location }}',
'{{ updateTime }}',
'{{ cloudConsoleUri }}',
true|false,
'{{ statusMessage }}',
'{{ customId }}',
'{{ pod }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: instances
        value: '{{ instances }}'
      - name: networks
        value: '{{ networks }}'
      - name: volumes
        value: '{{ volumes }}'
      - name: ticketId
        value: '{{ ticketId }}'
      - name: handoverServiceAccount
        value: '{{ handoverServiceAccount }}'
      - name: email
        value: '{{ email }}'
      - name: state
        value: '{{ state }}'
      - name: location
        value: '{{ location }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: cloudConsoleUri
        value: '{{ cloudConsoleUri }}'
      - name: vpcScEnabled
        value: '{{ vpcScEnabled }}'
      - name: statusMessage
        value: '{{ statusMessage }}'
      - name: customId
        value: '{{ customId }}'
      - name: pod
        value: '{{ pod }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a provisioning_config only if the necessary resources are available.

```sql
UPDATE google.baremetalsolution.provisioning_configs
SET 
name = '{{ name }}',
instances = '{{ instances }}',
networks = '{{ networks }}',
volumes = '{{ volumes }}',
ticketId = '{{ ticketId }}',
handoverServiceAccount = '{{ handoverServiceAccount }}',
email = '{{ email }}',
state = '{{ state }}',
location = '{{ location }}',
updateTime = '{{ updateTime }}',
cloudConsoleUri = '{{ cloudConsoleUri }}',
vpcScEnabled = true|false,
statusMessage = '{{ statusMessage }}',
customId = '{{ customId }}',
pod = '{{ pod }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND provisioningConfigsId = '{{ provisioningConfigsId }}';
```
