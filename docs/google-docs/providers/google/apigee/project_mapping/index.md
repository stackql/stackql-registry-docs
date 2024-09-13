
---
title: project_mapping
hide_title: false
hide_table_of_contents: false
keywords:
  - project_mapping
  - apigee
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

Creates, updates, deletes or gets an <code>project_mapping</code> resource or lists <code>project_mapping</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>project_mapping</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.project_mapping" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Output only. The Google Cloud region where control plane data is located. For more information, see https://cloud.google.com/about/locations/. |
| <CopyableCode code="organization" /> | `string` | Name of the Apigee organization. |
| <CopyableCode code="projectId" /> | `string` | Google Cloud project associated with the Apigee organization |
| <CopyableCode code="projectIds" /> | `array` | DEPRECATED: Use `project_id`. An Apigee Organization is mapped to a single project. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_get_project_mapping" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Gets the project ID and region for an Apigee organization. |

## `SELECT` examples

Gets the project ID and region for an Apigee organization.

```sql
SELECT
location,
organization,
projectId,
projectIds
FROM google.apigee.project_mapping
WHERE organizationsId = '{{ organizationsId }}'; 
```
