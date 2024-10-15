---
title: organizations_elastic_to_azure_subscription_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations_elastic_to_azure_subscription_mappings
  - elastic
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

Creates, updates, deletes, gets or lists a <code>organizations_elastic_to_azure_subscription_mappings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organizations_elastic_to_azure_subscription_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.elastic.organizations_elastic_to_azure_subscription_mappings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of Azure Subscription ID to which the Organization of the logged in user belongs and gets billed into. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get Elastic Organization To Azure Subscription Mapping details for the logged-in user. |

## `SELECT` examples

Get Elastic Organization To Azure Subscription Mapping details for the logged-in user.


```sql
SELECT
properties
FROM azure_isv.elastic.organizations_elastic_to_azure_subscription_mappings
WHERE subscriptionId = '{{ subscriptionId }}';
```