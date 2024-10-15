---
title: factories_github_access_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - factories_github_access_tokens
  - data_factory
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

Creates, updates, deletes, gets or lists a <code>factories_github_access_tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>factories_github_access_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.factories_github_access_tokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="gitHubAccessToken" /> | `string` | GitHub access token. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId, data__gitHubAccessCode, data__gitHubAccessTokenBaseUrl" /> | Get GitHub Access Token. |

## `SELECT` examples

Get GitHub Access Token.


```sql
SELECT
gitHubAccessToken
FROM azure.data_factory.factories_github_access_tokens
WHERE factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__gitHubAccessCode = '{{ data__gitHubAccessCode }}'
AND data__gitHubAccessTokenBaseUrl = '{{ data__gitHubAccessTokenBaseUrl }}';
```