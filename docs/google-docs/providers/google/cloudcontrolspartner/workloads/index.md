---
title: workloads
hide_title: false
hide_table_of_contents: false
keywords:
  - workloads
  - cloudcontrolspartner
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
<tr><td><b>Name</b></td><td><code>workloads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudcontrolspartner.workloads" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Format: `organizations/&#123;organization&#125;/locations/&#123;location&#125;/customers/&#123;customer&#125;/workloads/&#123;workload&#125;` |
| <CopyableCode code="createTime" /> | `string` | Output only. Time the resource was created. |
| <CopyableCode code="folder" /> | `string` | Output only. The name of container folder of the assured workload |
| <CopyableCode code="folderId" /> | `string` | Output only. Folder id this workload is associated with |
| <CopyableCode code="isOnboarded" /> | `boolean` | Indicates whether a workload is fully onboarded. |
| <CopyableCode code="keyManagementProjectId" /> | `string` | The project id of the key management project for the workload |
| <CopyableCode code="location" /> | `string` | The Google Cloud location of the workload |
| <CopyableCode code="partner" /> | `string` | Partner associated with this workload. |
| <CopyableCode code="workloadOnboardingState" /> | `object` | Container for workload onboarding steps. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customersId, locationsId, organizationsId, workloadsId" /> | Gets details of a single workload |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="customersId, locationsId, organizationsId" /> | Lists customer workloads for a given customer org id |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="customersId, locationsId, organizationsId" /> | Lists customer workloads for a given customer org id |
