---
title: documents_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - documents_list_only
  - ssm
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>documents</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/documents/"><code>documents</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>documents_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SSM::Document resource is an SSM document in AWS Systems Manager that defines the actions that Systems Manager performs, which can be used to set up and run commands on your instances.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssm.documents_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="content" /></td><td><code>object</code></td><td>The content for the Systems Manager document in JSON, YAML or String format.</td></tr>
<tr><td><CopyableCode code="attachments" /></td><td><code>array</code></td><td>A list of key and value pairs that describe attachments to a version of a document.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the Systems Manager document.</td></tr>
<tr><td><CopyableCode code="version_name" /></td><td><code>string</code></td><td>An optional field specifying the version of the artifact you are creating with the document. This value is unique across all versions of a document, and cannot be changed.</td></tr>
<tr><td><CopyableCode code="document_type" /></td><td><code>string</code></td><td>The type of document to create.</td></tr>
<tr><td><CopyableCode code="document_format" /></td><td><code>string</code></td><td>Specify the document format for the request. The document format can be either JSON or YAML. JSON is the default format.</td></tr>
<tr><td><CopyableCode code="target_type" /></td><td><code>string</code></td><td>Specify a target type to define the kinds of resources the document can run on.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment.</td></tr>
<tr><td><CopyableCode code="requires" /></td><td><code>array</code></td><td>A list of SSM documents required by a document. For example, an ApplicationConfiguration document requires an ApplicationConfigurationSchema document.</td></tr>
<tr><td><CopyableCode code="update_method" /></td><td><code>string</code></td><td>Update method - when set to 'Replace', the update will replace the existing document; when set to 'NewVersion', the update will create a new version.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>documents</code> in a region.
```sql
SELECT
region,
name
FROM aws.ssm.documents_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>documents_list_only</code> resource, see <a href="/providers/aws/ssm/documents/#permissions"><code>documents</code></a>


