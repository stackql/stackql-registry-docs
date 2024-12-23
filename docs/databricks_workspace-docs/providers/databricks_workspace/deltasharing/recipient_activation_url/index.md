---
title: recipient_activation_url
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - recipient_activation_url
  - deltasharing
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

Operations on a <code>recipient_activation_url</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recipient_activation_url</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.deltasharing.recipient_activation_url" /></td></tr>
</tbody></table>


`SELECT` not supported for this resource, see the methods section for supported operations.
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getactivationurlinfo" /> | `EXEC` | <CopyableCode code="activation_url, deployment_name" /> | Gets an activation URL for a share. |
