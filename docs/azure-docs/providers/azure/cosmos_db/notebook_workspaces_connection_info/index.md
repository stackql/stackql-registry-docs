---
title: notebook_workspaces_connection_info
hide_title: false
hide_table_of_contents: false
keywords:
  - notebook_workspaces_connection_info
  - cosmos_db
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

Creates, updates, deletes, gets or lists a <code>notebook_workspaces_connection_info</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notebook_workspaces_connection_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.notebook_workspaces_connection_info" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="authToken" /> | `string` | Specifies auth token used for connecting to Notebook server (uses token-based auth). |
| <CopyableCode code="notebookServerEndpoint" /> | `string` | Specifies the endpoint of Notebook server. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, notebookWorkspaceName, resourceGroupName, subscriptionId" /> | Retrieves the connection info for the notebook workspace |

## `SELECT` examples

Retrieves the connection info for the notebook workspace


```sql
SELECT
authToken,
notebookServerEndpoint
FROM azure.cosmos_db.notebook_workspaces_connection_info
WHERE accountName = '{{ accountName }}'
AND notebookWorkspaceName = '{{ notebookWorkspaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```