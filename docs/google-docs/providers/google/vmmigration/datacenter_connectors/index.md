---
title: datacenter_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - datacenter_connectors
  - vmmigration
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

Creates, updates, deletes, gets or lists a <code>datacenter_connectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datacenter_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmmigration.datacenter_connectors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The connector's name. |
| <CopyableCode code="applianceInfrastructureVersion" /> | `string` | Output only. Appliance OVA version. This is the OVA which is manually installed by the user and contains the infrastructure for the automatically updatable components on the appliance. |
| <CopyableCode code="applianceSoftwareVersion" /> | `string` | Output only. Appliance last installed update bundle version. This is the version of the automatically updatable components on the appliance. |
| <CopyableCode code="availableVersions" /> | `object` | Holds informatiom about the available versions for upgrade. |
| <CopyableCode code="bucket" /> | `string` | Output only. The communication channel between the datacenter connector and Google Cloud. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the connector was created (as an API call, not when it was actually installed). |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="registrationId" /> | `string` | Immutable. A unique key for this connector. This key is internal to the OVA connector and is supplied with its creation during the registration process and can not be modified. |
| <CopyableCode code="serviceAccount" /> | `string` | The service account to use in the connector when communicating with the cloud. |
| <CopyableCode code="state" /> | `string` | Output only. State of the DatacenterConnector, as determined by the health checks. |
| <CopyableCode code="stateTime" /> | `string` | Output only. The time the state was last set. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last time the connector was updated with an API call. |
| <CopyableCode code="upgradeStatus" /> | `object` | UpgradeStatus contains information about upgradeAppliance operation. |
| <CopyableCode code="version" /> | `string` | The version running in the DatacenterConnector. This is supplied by the OVA connector during the registration process and can not be modified. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="datacenterConnectorsId, locationsId, projectsId, sourcesId" /> | Gets details of a single DatacenterConnector. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, sourcesId" /> | Lists DatacenterConnectors in a given Source. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, sourcesId" /> | Creates a new DatacenterConnector in a given Source. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="datacenterConnectorsId, locationsId, projectsId, sourcesId" /> | Deletes a single DatacenterConnector. |
| <CopyableCode code="upgrade_appliance" /> | `EXEC` | <CopyableCode code="datacenterConnectorsId, locationsId, projectsId, sourcesId" /> | Upgrades the appliance relate to this DatacenterConnector to the in-place updateable version. |

## `SELECT` examples

Lists DatacenterConnectors in a given Source.

```sql
SELECT
name,
applianceInfrastructureVersion,
applianceSoftwareVersion,
availableVersions,
bucket,
createTime,
error,
registrationId,
serviceAccount,
state,
stateTime,
updateTime,
upgradeStatus,
version
FROM google.vmmigration.datacenter_connectors
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND sourcesId = '{{ sourcesId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>datacenter_connectors</code> resource.

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
INSERT INTO google.vmmigration.datacenter_connectors (
locationsId,
projectsId,
sourcesId,
registrationId,
serviceAccount,
version
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ sourcesId }}',
'{{ registrationId }}',
'{{ serviceAccount }}',
'{{ version }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: name
      value: string
    - name: registrationId
      value: string
    - name: serviceAccount
      value: string
    - name: version
      value: string
    - name: bucket
      value: string
    - name: state
      value: string
    - name: stateTime
      value: string
    - name: error
      value:
        - name: code
          value: integer
        - name: message
          value: string
        - name: details
          value:
            - object
    - name: applianceInfrastructureVersion
      value: string
    - name: applianceSoftwareVersion
      value: string
    - name: availableVersions
      value:
        - name: newDeployableAppliance
          value:
            - name: version
              value: string
            - name: uri
              value: string
            - name: critical
              value: boolean
            - name: releaseNotesUri
              value: string
    - name: upgradeStatus
      value:
        - name: version
          value: string
        - name: state
          value: string
        - name: startTime
          value: string
        - name: previousVersion
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>datacenter_connectors</code> resource.

```sql
/*+ delete */
DELETE FROM google.vmmigration.datacenter_connectors
WHERE datacenterConnectorsId = '{{ datacenterConnectorsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND sourcesId = '{{ sourcesId }}';
```
