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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>workload</code> resource or lists <code>workloads</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workloads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudcontrolspartner.workloads" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}` |
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

## `SELECT` examples

Lists customer workloads for a given customer org id

```sql
SELECT
name,
createTime,
folder,
folderId,
isOnboarded,
keyManagementProjectId,
location,
partner,
workloadOnboardingState
FROM google.cloudcontrolspartner.workloads
WHERE customersId = '{{ customersId }}'
AND locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}'; 
```
