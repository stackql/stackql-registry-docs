---
title: flux_config_operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - flux_config_operation_status
  - kubernetes_configuration
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

Creates, updates, deletes, gets or lists a <code>flux_config_operation_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flux_config_operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.kubernetes_configuration.flux_config_operation_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified ID for the async operation. |
| <CopyableCode code="name" /> | `string` | Name of the async operation. |
| <CopyableCode code="error" /> | `object` | The error detail. |
| <CopyableCode code="properties" /> | `object` | Additional information, if available. |
| <CopyableCode code="status" /> | `string` | Operation status. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, fluxConfigurationName, operationId, resourceGroupName, subscriptionId" /> | Get Async Operation status |

## `SELECT` examples

Get Async Operation status


```sql
SELECT
id,
name,
error,
properties,
status
FROM azure.kubernetes_configuration.flux_config_operation_status
WHERE clusterName = '{{ clusterName }}'
AND clusterResourceName = '{{ clusterResourceName }}'
AND clusterRp = '{{ clusterRp }}'
AND fluxConfigurationName = '{{ fluxConfigurationName }}'
AND operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```