---
title: organizations_all_serverless_runtimes
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations_all_serverless_runtimes
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

Creates, updates, deletes, gets or lists a <code>organizations_all_serverless_runtimes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organizations_all_serverless_runtimes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.informatica.organizations_all_serverless_runtimes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="informaticaRuntimeResources" /> | `array` | List of runtime resources for the fetch all API |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> | Gets all serverless runtime resources in a given informatica organization resource. |

## `SELECT` examples

Gets all serverless runtime resources in a given informatica organization resource.


```sql
SELECT
informaticaRuntimeResources
FROM azure_isv.informatica.organizations_all_serverless_runtimes
WHERE organizationName = '{{ organizationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```