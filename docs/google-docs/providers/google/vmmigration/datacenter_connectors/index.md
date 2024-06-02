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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datacenter_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vmmigration.datacenter_connectors" /></td></tr>
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
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, sourcesId" /> | Lists DatacenterConnectors in a given Source. |
| <CopyableCode code="upgrade_appliance" /> | `EXEC` | <CopyableCode code="datacenterConnectorsId, locationsId, projectsId, sourcesId" /> | Upgrades the appliance relate to this DatacenterConnector to the in-place updateable version. |
