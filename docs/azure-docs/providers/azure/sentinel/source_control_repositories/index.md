---
title: source_control_repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - source_control_repositories
  - sentinel
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

Creates, updates, deletes, gets or lists a <code>source_control_repositories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>source_control_repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.source_control_repositories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="branches" /> | `array` | Array of branches. |
| <CopyableCode code="fullName" /> | `string` | The name of the repository. |
| <CopyableCode code="installationId" /> | `integer` | The installation id of the repository. |
| <CopyableCode code="url" /> | `string` | The url to access the repository. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName, data__properties" /> | Gets a list of repositories metadata. |

## `SELECT` examples

Gets a list of repositories metadata.


```sql
SELECT
branches,
fullName,
installationId,
url
FROM azure.sentinel.source_control_repositories
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}'
AND data__properties = '{{ data__properties }}';
```