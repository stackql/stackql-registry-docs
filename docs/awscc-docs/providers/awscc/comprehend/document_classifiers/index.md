---
title: document_classifiers
hide_title: false
hide_table_of_contents: false
keywords:
  - document_classifiers
  - comprehend
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>document_classifiers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>document_classifiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>document_classifiers</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.comprehend.document_classifiers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>document_classifiers</code> resource, the following permissions are required:

### Create
<pre>
iam:PassRole,
comprehend:CreateDocumentClassifier,
comprehend:DescribeDocumentClassifier,
comprehend:DescribeResourcePolicy,
comprehend:ListTagsForResource,
textract:DetectDocumentText</pre>

### List
<pre>
comprehend:ListDocumentClassifiers</pre>


## Example
```sql
SELECT
region,
arn
FROM awscc.comprehend.document_classifiers
WHERE region = 'us-east-1'
```
