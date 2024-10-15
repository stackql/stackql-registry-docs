---
title: manager_deployment_status
hide_title: false
hide_table_of_contents: false
keywords:
  - manager_deployment_status
  - network
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

Creates, updates, deletes, gets or lists a <code>manager_deployment_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>manager_deployment_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.manager_deployment_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="commitTime" /> | `string` | Commit Time. |
| <CopyableCode code="configurationIds" /> | `array` | List of configuration ids. |
| <CopyableCode code="deploymentStatus" /> | `string` | Deployment Status. |
| <CopyableCode code="deploymentType" /> | `string` | Configuration Deployment Type. |
| <CopyableCode code="errorMessage" /> | `string` | Error Message. |
| <CopyableCode code="region" /> | `string` | Region Name. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkManagerName, resourceGroupName, subscriptionId" /> | Post to List of Network Manager Deployment Status. |

## `SELECT` examples

Post to List of Network Manager Deployment Status.


```sql
SELECT
commitTime,
configurationIds,
deploymentStatus,
deploymentType,
errorMessage,
region
FROM azure.network.manager_deployment_status
WHERE networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```