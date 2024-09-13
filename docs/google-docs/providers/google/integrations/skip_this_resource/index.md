---
title: skip_this_resource
hide_title: false
hide_table_of_contents: false
keywords:
  - skip_this_resource
  - integrations
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

Creates, updates, deletes or gets an <code>skip_this_resource</code> resource or lists <code>skip_this_resource</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>skip_this_resource</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.integrations.skip_this_resource" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_integrations_execute_event" /> | `EXEC` | <CopyableCode code="integrationsId, locationsId, projectsId" /> | Executes an integration on receiving events from Integration Connector triggers, Eventarc or CPS Trigger. Input data to integration is received in body in json format |
