---
title: gateways_env_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - gateways_env_secrets
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

Creates, updates, deletes, gets or lists a <code>gateways_env_secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateways_env_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.gateways_env_secrets" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="gatewayName, resourceGroupName, serviceName, subscriptionId" /> | List sensitive environment variables of Spring Cloud Gateway. |

## `SELECT` examples

List sensitive environment variables of Spring Cloud Gateway.


```sql
SELECT

FROM azure.spring_apps.gateways_env_secrets
WHERE gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```