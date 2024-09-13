---
title: example_comparisons
hide_title: false
hide_table_of_contents: false
keywords:
  - example_comparisons
  - datalabeling
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

Creates, updates, deletes, gets or lists a <code>example_comparisons</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>example_comparisons</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datalabeling.example_comparisons" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_datasets_evaluations_example_comparisons_search" /> | `EXEC` | <CopyableCode code="datasetsId, evaluationsId, projectsId" /> | Searches example comparisons from an evaluation. The return format is a list of example comparisons that show ground truth and prediction(s) for a single input. Search by providing an evaluation ID. |
