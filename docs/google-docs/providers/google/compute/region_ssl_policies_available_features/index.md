---
title: region_ssl_policies_available_features
hide_title: false
hide_table_of_contents: false
keywords:
  - region_ssl_policies_available_features
  - compute
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

Creates, updates, deletes or gets an <code>region_ssl_policies_available_feature</code> resource or lists <code>region_ssl_policies_available_features</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_ssl_policies_available_features</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_ssl_policies_available_features" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="features" /> | `array` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_available_features" /> | `SELECT` | <CopyableCode code="project, region" /> | Lists all features that can be specified in the SSL policy when using custom profile. |

## `SELECT` examples

Lists all features that can be specified in the SSL policy when using custom profile.

```sql
SELECT
features
FROM google.compute.region_ssl_policies_available_features
WHERE project = '{{ project }}'
AND region = '{{ region }}'; 
```
