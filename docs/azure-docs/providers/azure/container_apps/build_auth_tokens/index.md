---
title: build_auth_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - build_auth_tokens
  - container_apps
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

Creates, updates, deletes, gets or lists a <code>build_auth_tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>build_auth_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.build_auth_tokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="expires" /> | `string` | Token expiration date. |
| <CopyableCode code="token" /> | `string` | Authentication token. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="buildName, builderName, resourceGroupName, subscriptionId" /> | Gets the token used to connect to the endpoint where source code can be uploaded for a build. |

## `SELECT` examples

Gets the token used to connect to the endpoint where source code can be uploaded for a build.


```sql
SELECT
expires,
token
FROM azure.container_apps.build_auth_tokens
WHERE buildName = '{{ buildName }}'
AND builderName = '{{ builderName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```