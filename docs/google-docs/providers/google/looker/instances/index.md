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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="looker.instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/instances/&#123;instance&#125;`. |
| <CopyableCode code="adminSettings" /> | `object` | Looker instance Admin settings fields. |
| <CopyableCode code="consumerNetwork" /> | `string` | Network name in the consumer project. Format: `projects/&#123;project&#125;/global/networks/&#123;network&#125;`. Note that the consumer network may be in a different GCP project than the consumer project that is hosting the Looker Instance. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the Looker instance provisioning was first requested. |
| <CopyableCode code="customDomain" /> | `object` | Custom domain information. |
| <CopyableCode code="denyMaintenancePeriod" /> | `object` | Specifies the maintenance denial period. |
| <CopyableCode code="egressPublicIp" /> | `string` | Output only. Public Egress IP (IPv4). |
| <CopyableCode code="encryptionConfig" /> | `object` | Encryption configuration (i.e. CMEK). |
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
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists Instances in a given project and location. |
| <CopyableCode code="export" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Export instance. |
| <CopyableCode code="import" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Import instance. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Update Instance. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Restart instance. |
