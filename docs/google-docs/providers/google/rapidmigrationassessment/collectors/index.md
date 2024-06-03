---
title: collectors
hide_title: false
hide_table_of_contents: false
keywords:
  - collectors
  - rapidmigrationassessment
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
<tr><td><b>Name</b></td><td><code>collectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.rapidmigrationassessment.collectors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | name of resource. |
| <CopyableCode code="description" /> | `string` | User specified description of the Collector. |
| <CopyableCode code="bucket" /> | `string` | Output only. Store cloud storage bucket name (which is a guid) created with this Collector. |
| <CopyableCode code="clientVersion" /> | `string` | Output only. Client version. |
| <CopyableCode code="collectionDays" /> | `integer` | How many days to collect data. |
| <CopyableCode code="createTime" /> | `string` | Output only. Create time stamp. |
| <CopyableCode code="displayName" /> | `string` | User specified name of the Collector. |
| <CopyableCode code="eulaUri" /> | `string` | Uri for EULA (End User License Agreement) from customer. |
| <CopyableCode code="expectedAssetCount" /> | `string` | User specified expected asset count. |
| <CopyableCode code="guestOsScan" /> | `object` | Message describing a MC Source of type Guest OS Scan. |
| <CopyableCode code="labels" /> | `object` | Labels as key value pairs. |
| <CopyableCode code="serviceAccount" /> | `string` | Service Account email used to ingest data to this Collector. |
| <CopyableCode code="state" /> | `string` | Output only. State of the Collector. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Update time stamp. |
| <CopyableCode code="vsphereScan" /> | `object` | Message describing a MC Source of type VSphere Scan. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="collectorsId, locationsId, projectsId" /> | Gets details of a single Collector. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Collectors in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a Collector to manage the on-prem appliance which collects information about Customer assets. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="collectorsId, locationsId, projectsId" /> | Deletes a single Collector - changes state of collector to "Deleting". Background jobs does final deletion thorugh producer api. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="collectorsId, locationsId, projectsId" /> | Updates the parameters of a single Collector. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists Collectors in a given project and location. |
| <CopyableCode code="pause" /> | `EXEC` | <CopyableCode code="collectorsId, locationsId, projectsId" /> | Pauses the given collector. |
| <CopyableCode code="register" /> | `EXEC` | <CopyableCode code="collectorsId, locationsId, projectsId" /> | Registers the given collector. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="collectorsId, locationsId, projectsId" /> | Resumes the given collector. |
