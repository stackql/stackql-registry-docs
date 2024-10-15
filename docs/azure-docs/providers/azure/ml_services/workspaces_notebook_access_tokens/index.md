---
title: workspaces_notebook_access_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces_notebook_access_tokens
  - ml_services
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

Creates, updates, deletes, gets or lists a <code>workspaces_notebook_access_tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces_notebook_access_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.workspaces_notebook_access_tokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accessToken" /> | `string` |  |
| <CopyableCode code="expiresIn" /> | `integer` |  |
| <CopyableCode code="hostName" /> | `string` |  |
| <CopyableCode code="notebookResourceId" /> | `string` |  |
| <CopyableCode code="publicDns" /> | `string` |  |
| <CopyableCode code="refreshToken" /> | `string` |  |
| <CopyableCode code="scope" /> | `string` |  |
| <CopyableCode code="tokenType" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |  |

## `SELECT` examples




```sql
SELECT
accessToken,
expiresIn,
hostName,
notebookResourceId,
publicDns,
refreshToken,
scope,
tokenType
FROM azure.ml_services.workspaces_notebook_access_tokens
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```