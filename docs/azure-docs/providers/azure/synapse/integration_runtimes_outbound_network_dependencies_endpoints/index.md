---
title: integration_runtimes_outbound_network_dependencies_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtimes_outbound_network_dependencies_endpoints
  - synapse
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

Creates, updates, deletes, gets or lists a <code>integration_runtimes_outbound_network_dependencies_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_runtimes_outbound_network_dependencies_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.integration_runtimes_outbound_network_dependencies_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="category" /> | `string` | The category of outbound network dependency. |
| <CopyableCode code="endpoints" /> | `array` | The endpoints for outbound network dependency. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName" /> | Gets the list of outbound network dependencies for a given Azure-SSIS integration runtime. |

## `SELECT` examples

Gets the list of outbound network dependencies for a given Azure-SSIS integration runtime.


```sql
SELECT
category,
endpoints
FROM azure.synapse.integration_runtimes_outbound_network_dependencies_endpoints
WHERE integrationRuntimeName = '{{ integrationRuntimeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```