---
title: eureka_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - eureka_servers
  - spring_apps
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

Creates, updates, deletes, gets or lists a <code>eureka_servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>eureka_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.eureka_servers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Eureka server properties payload |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Get the eureka server settings. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | List the eureka server settings. |
| <CopyableCode code="update_patch" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Update the eureka server settings. |
| <CopyableCode code="update_put" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Update the eureka server settings. |

## `SELECT` examples

Get the eureka server settings.


```sql
SELECT
properties
FROM azure.spring_apps.eureka_servers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```