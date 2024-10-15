---
title: adc_catalogst_by_resource_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - adc_catalogst_by_resource_groups
  - data_catalog
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

Creates, updates, deletes, gets or lists a <code>adc_catalogst_by_resource_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>adc_catalogst_by_resource_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_catalog.adc_catalogst_by_resource_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="etag" /> | `string` | Resource etag |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Properties of the data catalog. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The List catalogs in Resource Group operation lists all the Azure Data Catalogs available under the given resource group. |

## `SELECT` examples

The List catalogs in Resource Group operation lists all the Azure Data Catalogs available under the given resource group.


```sql
SELECT
id,
name,
etag,
location,
properties,
tags,
type
FROM azure.data_catalog.adc_catalogst_by_resource_groups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```