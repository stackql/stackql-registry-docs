---
title: config
hide_title: false
hide_table_of_contents: false
keywords:
  - config
  - ml
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

Creates, updates, deletes or gets an <code>config</code> resource or lists <code>config</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.ml.config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="config" /> | `object` |  |
| <CopyableCode code="serviceAccount" /> | `string` | The service account Cloud ML uses to access resources in the project. |
| <CopyableCode code="serviceAccountProject" /> | `string` | The project number for `service_account`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_get_config" /> | `SELECT` | <CopyableCode code="projectsId" /> | Get the service account information associated with your project. You need this information in order to grant the service account permissions for the Google Cloud Storage location where you put your model training code for training the model with Google Cloud Machine Learning. |

## `SELECT` examples

Get the service account information associated with your project. You need this information in order to grant the service account permissions for the Google Cloud Storage location where you put your model training code for training the model with Google Cloud Machine Learning.

```sql
SELECT
config,
serviceAccount,
serviceAccountProject
FROM google.ml.config
WHERE projectsId = '{{ projectsId }}'; 
```
