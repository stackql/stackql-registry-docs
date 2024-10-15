---
title: kusto_pool_child_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - kusto_pool_child_resources
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

Creates, updates, deletes, gets or lists a <code>kusto_pool_child_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kusto_pool_child_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.kusto_pool_child_resources" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__name, data__type" /> | Checks that the Kusto Pool child resource name is valid and is not already in use. |
