---
title: recipient_activation_token
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - recipient_activation_token
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

Operations on a <code>recipient_activation_token</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recipient_activation_token</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.deltasharing.recipient_activation_token" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="bearerToken" /> | `string` |
| <CopyableCode code="endpoint" /> | `string` |
| <CopyableCode code="expirationTime" /> | `string` |
| <CopyableCode code="shareCredentialsVersion" /> | `integer` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="retrievetoken" /> | `SELECT` | <CopyableCode code="activation_url, deployment_name" /> | Retrieve access token with an activation url. This is a public API without any authentication. |

## `SELECT` examples

```sql
SELECT
bearerToken,
endpoint,
expirationTime,
shareCredentialsVersion
FROM databricks_workspace.deltasharing.recipient_activation_token
WHERE activation_url = '{{ activation_url }}' AND
deployment_name = '{{ deployment_name }}';
```
