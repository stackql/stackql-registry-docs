
---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
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

Creates, updates, deletes or gets an <code>project</code> resource or lists <code>projects</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.ml.projects" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_explain" /> | `EXEC` | <CopyableCode code="projectsId" /> | Performs explanation on the data in the request. {% dynamic include "/ai-platform/includes/___explain-request" %}  |
| <CopyableCode code="projects_predict" /> | `EXEC` | <CopyableCode code="projectsId" /> | Performs online prediction on the data in the request. {% dynamic include "/ai-platform/includes/___predict-request" %}  |
