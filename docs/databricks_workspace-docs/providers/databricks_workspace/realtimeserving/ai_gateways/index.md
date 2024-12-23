---
title: ai_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - ai_gateways
  - realtimeserving
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_workspace/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>ai_gateways</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ai_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.realtimeserving.ai_gateways" /></td></tr>
</tbody></table>


`SELECT` not supported for this resource, see the methods section for supported operations.
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="putaigateway" /> | `EXEC` | <CopyableCode code="name, deployment_name" /> | Used to update the AI Gateway of a serving endpoint. NOTE: Only external model endpoints are currently supported. |
