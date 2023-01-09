---
title: labels
hide_title: false
hide_table_of_contents: false
keywords:
  - labels
  - drivelabels
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.drivelabels.labels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Output only. Globally unique identifier of this label. ID makes up part of the label `name`, but unlike `name`, ID is consistent between revisions. Matches the regex: `([a-zA-Z0-9])+` |
| `name` | `string` | Output only. Resource name of the label. Will be in the form of either: `labels/&#123;id&#125;` or `labels/&#123;id&#125;@&#123;revision_id&#125;` depending on the request. See `id` and `revision_id` below. |
| `disabler` | `object` | Information about a user. |
| `lifecycle` | `object` | The lifecycle state of an object, such as label, field, or choice. The lifecycle enforces the following transitions: * `UNPUBLISHED_DRAFT` (starting state) * `UNPUBLISHED_DRAFT` -&gt; `PUBLISHED` * `UNPUBLISHED_DRAFT` -&gt; (Deleted) * `PUBLISHED` -&gt; `DISABLED` * `DISABLED` -&gt; `PUBLISHED` * `DISABLED` -&gt; (Deleted) The published and disabled states have some distinct characteristics: * Published—Some kinds of changes might be made to an object in this state, in which case `has_unpublished_changes` will be true. Also, some kinds of changes are not permitted. Generally, any change that would invalidate or cause new restrictions on existing metadata related to the label are rejected. * Disabled—When disabled, the configured `DisabledPolicy` takes effect. |
| `appliedLabelPolicy` | `object` | Behavior of this label when it's applied to Drive items. |
| `labelType` | `string` | Required. The type of label. |
| `revisionId` | `string` | Output only. Revision ID of the label. Revision ID might be part of the label `name` depending on the request issued. A new revision is created whenever revisioned properties of a label are changed. Matches the regex: `([a-zA-Z0-9])+` |
| `createTime` | `string` | Output only. The time this label was created. |
| `creator` | `object` | Information about a user. |
| `publisher` | `object` | Information about a user. |
| `appliedCapabilities` | `object` | The capabilities a user has on this label's applied metadata. |
| `displayHints` | `object` | UI display hints for rendering the label. |
| `lockStatus` | `object` | Contains information about whether a label component should be considered locked. |
| `revisionCreator` | `object` | Information about a user. |
| `fields` | `array` | List of fields in descending priority order. |
| `publishTime` | `string` | Output only. The time this label was published. This value has no meaning when the label is not published. |
| `disableTime` | `string` | Output only. The time this label was disabled. This value has no meaning when the label is not disabled. |
| `revisionCreateTime` | `string` | Output only. The time this label revision was created. |
| `properties` | `object` | Basic properties of the label. |
| `schemaCapabilities` | `object` | The capabilities related to this label when editing the label. |
| `learnMoreUri` | `string` | Custom URL to present to users to allow them to learn more about this label and how it should be used. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `labelsId` | Get a label by its resource name. Resource name may be any of: * `labels/&#123;id&#125;` - See `labels/&#123;id&#125;@latest` * `labels/&#123;id&#125;@latest` - Gets the latest revision of the label. * `labels/&#123;id&#125;@published` - Gets the current published revision of the label. * `labels/&#123;id&#125;@&#123;revision_id&#125;` - Gets the label at the specified revision ID. |
| `list` | `SELECT` |  | List labels. |
