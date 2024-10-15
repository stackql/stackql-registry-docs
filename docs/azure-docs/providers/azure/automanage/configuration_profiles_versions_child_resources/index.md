---
title: configuration_profiles_versions_child_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_profiles_versions_child_resources
  - automanage
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

Creates, updates, deletes, gets or lists a <code>configuration_profiles_versions_child_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_profiles_versions_child_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automanage.configuration_profiles_versions_child_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Automanage configuration profile properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="configurationProfileName, resourceGroupName, subscriptionId" /> | Retrieve a list of configuration profile version for a configuration profile  |

## `SELECT` examples

Retrieve a list of configuration profile version for a configuration profile 


```sql
SELECT
location,
properties,
systemData,
tags
FROM azure.automanage.configuration_profiles_versions_child_resources
WHERE configurationProfileName = '{{ configurationProfileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```