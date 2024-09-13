---
title: environments_database_properties
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_database_properties
  - composer
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

Creates, updates, deletes or gets an <code>environments_database_property</code> resource or lists <code>environments_database_properties</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments_database_properties</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.composer.environments_database_properties" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="isFailoverReplicaAvailable" /> | `boolean` | The availability status of the failover replica. A false status indicates that the failover replica is out of sync. The primary instance can only fail over to the failover replica when the status is true. |
| <CopyableCode code="primaryGceZone" /> | `string` | The Compute Engine zone that the instance is currently serving from. |
| <CopyableCode code="secondaryGceZone" /> | `string` | The Compute Engine zone that the failover instance is currently serving from for a regional Cloud SQL instance. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_database_properties" /> | `SELECT` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Fetches database properties. |

## `SELECT` examples

Fetches database properties.

```sql
SELECT
isFailoverReplicaAvailable,
primaryGceZone,
secondaryGceZone
FROM google.composer.environments_database_properties
WHERE environmentsId = '{{ environmentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
