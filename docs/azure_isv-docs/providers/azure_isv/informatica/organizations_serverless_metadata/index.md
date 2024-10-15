---
title: organizations_serverless_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations_serverless_metadata
  - informatica
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

Creates, updates, deletes, gets or lists a <code>organizations_serverless_metadata</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organizations_serverless_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.informatica.organizations_serverless_metadata" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="serverlessConfigProperties" /> | `object` | Metadata Serverless Config Properties |
| <CopyableCode code="serverlessRuntimeConfigProperties" /> | `object` | Serverless Runtime config properties. |
| <CopyableCode code="type" /> | `string` | Various types of the runtime types. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> | Gets Metadata of the serverless runtime environment. |

## `SELECT` examples

Gets Metadata of the serverless runtime environment.


```sql
SELECT
serverlessConfigProperties,
serverlessRuntimeConfigProperties,
type
FROM azure_isv.informatica.organizations_serverless_metadata
WHERE organizationName = '{{ organizationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```