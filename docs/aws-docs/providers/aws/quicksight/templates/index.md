---
title: templates
hide_title: false
hide_table_of_contents: false
keywords:
  - templates
  - quicksight
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


Used to retrieve a list of <code>templates</code> in a region or to create or delete a <code>templates</code> resource, use <code>template</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::Template Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="template_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="AwsAccountId, TemplateId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
aws_account_id,
template_id
FROM aws.quicksight.templates
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>template</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.quicksight.templates (
 AwsAccountId,
 TemplateId,
 region
)
SELECT 
'{{ AwsAccountId }}',
 '{{ TemplateId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.quicksight.templates (
 AwsAccountId,
 Definition,
 Name,
 Permissions,
 SourceEntity,
 Tags,
 TemplateId,
 ValidationStrategy,
 VersionDescription,
 region
)
SELECT 
 '{{ AwsAccountId }}',
 '{{ Definition }}',
 '{{ Name }}',
 '{{ Permissions }}',
 '{{ SourceEntity }}',
 '{{ Tags }}',
 '{{ TemplateId }}',
 '{{ ValidationStrategy }}',
 '{{ VersionDescription }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: template
    props:
      - name: AwsAccountId
        value: '{{ AwsAccountId }}'
      - name: Definition
        value:
          DataSetConfigurations:
            - Placeholder: '{{ Placeholder }}'
              DataSetSchema:
                ColumnSchemaList:
                  - Name: '{{ Name }}'
                    DataType: '{{ DataType }}'
                    GeographicRole: '{{ GeographicRole }}'
              ColumnGroupSchemaList:
                - Name: '{{ Name }}'
                  ColumnGroupColumnSchemaList:
                    - Name: '{{ Name }}'
          Sheets:
            - SheetId: '{{ SheetId }}'
              Title: '{{ Title }}'
              Description: '{{ Description }}'
              Name: '{{ Name }}'
              ParameterControls:
                - DateTimePicker:
                    ParameterControlId: '{{ ParameterControlId }}'
                    Title: '{{ Title }}'
                    SourceParameterName: '{{ SourceParameterName }}'
                    DisplayOptions:
                      TitleOptions:
                        Visibility: '{{ Visibility }}'
                        FontConfiguration:
                          FontSize:
                            Relative: '{{ Relative }}'
                          FontDecoration: '{{ FontDecoration }}'
                          FontColor: '{{ FontColor }}'
                          FontWeight:
                            Name: '{{ Name }}'
                          FontStyle: '{{ FontStyle }}'
                        CustomLabel: '{{ CustomLabel }}'
                      DateTimeFormat: '{{ DateTimeFormat }}'
                      InfoIconLabelOptions:
                        Visibility: null
                        InfoIconText: '{{ InfoIconText }}'
                  List:
                    ParameterControlId: '{{ ParameterControlId }}'
                    Title: '{{ Title }}'
                    SourceParameterName: '{{ SourceParameterName }}'
                    DisplayOptions:
                      SearchOptions:
                        Visibility: null
                      SelectAllOptions:
                        Visibility: null
                      TitleOptions: null
                      InfoIconLabelOptions: null
                    Type: '{{ Type }}'
                    SelectableValues:
                      Values:
                        - '{{ Values[0] }}'
                      LinkToDataSetColumn:
                        DataSetIdentifier: '{{ DataSetIdentifier }}'
                        ColumnName: '{{ ColumnName }}'
                    CascadingControlConfiguration:
                      SourceControls:
                        - SourceSheetControlId: '{{ SourceSheetControlId }}'
                          ColumnToMatch: null
                  Dropdown:
                    ParameterControlId: '{{ ParameterControlId }}'
                    Title: '{{ Title }}'
                    SourceParameterName: '{{ SourceParameterName }}'
                    DisplayOptions:
                      SelectAllOptions: null
                      TitleOptions: null
                      InfoIconLabelOptions: null
                    Type: null
                    SelectableValues: null
                    CascadingControlConfiguration: null
                  TextField:
                    ParameterControlId: '{{ ParameterControlId }}'
                    Title: '{{ Title }}'
                    SourceParameterName: '{{ SourceParameterName }}'
                    DisplayOptions:
                      TitleOptions: null
                      PlaceholderOptions:
                        Visibility: null
                      InfoIconLabelOptions: null
                  TextArea:
                    ParameterControlId: '{{ ParameterControlId }}'
                    Title: '{{ Title }}'
                    SourceParameterName: '{{ SourceParameterName }}'
                    Delimiter: '{{ Delimiter }}'
                    DisplayOptions:
                      TitleOptions: null
                      PlaceholderOptions: null
                      InfoIconLabelOptions: null
                  Slider:
                    ParameterControlId: '{{ ParameterControlId }}'
                    Title: '{{ Title }}'
                    SourceParameterName: '{{ SourceParameterName }}'
                    DisplayOptions:
                      TitleOptions: null
                      InfoIconLabelOptions: null
                    MaximumValue: null
                    MinimumValue: null
                    StepSize: null
              FilterControls:
                - DateTimePicker:
                    FilterControlId: '{{ FilterControlId }}'
                    Title: '{{ Title }}'
                    SourceFilterId: '{{ SourceFilterId }}'
                    DisplayOptions: null
                    Type: '{{ Type }}'
                  List:
                    FilterControlId: '{{ FilterControlId }}'
                    Title: '{{ Title }}'
                    SourceFilterId: '{{ SourceFilterId }}'
                    DisplayOptions: null
                    Type: null
                    SelectableValues:
                      Values:
                        - '{{ Values[0] }}'
                    CascadingControlConfiguration: null
                  Dropdown:
                    FilterControlId: '{{ FilterControlId }}'
                    Title: '{{ Title }}'
                    SourceFilterId: '{{ SourceFilterId }}'
                    DisplayOptions: null
                    Type: null
                    SelectableValues: null
                    CascadingControlConfiguration: null
                  TextField:
                    FilterControlId: '{{ FilterControlId }}'
                    Title: '{{ Title }}'
                    SourceFilterId: '{{ SourceFilterId }}'
                    DisplayOptions: null
                  TextArea:
                    FilterControlId: '{{ FilterControlId }}'
                    Title: '{{ Title }}'
                    SourceFilterId: '{{ SourceFilterId }}'
                    Delimiter: '{{ Delimiter }}'
                    DisplayOptions: null
                  Slider:
                    FilterControlId: '{{ FilterControlId }}'
                    Title: '{{ Title }}'
                    SourceFilterId: '{{ SourceFilterId }}'
                    DisplayOptions: null
                    Type: '{{ Type }}'
                    MaximumValue: null
                    MinimumValue: null
                    StepSize: null
                  RelativeDateTime:
                    FilterControlId: '{{ FilterControlId }}'
                    Title: '{{ Title }}'
                    SourceFilterId: '{{ SourceFilterId }}'
                    DisplayOptions:
                      TitleOptions: null
                      DateTimeFormat: '{{ DateTimeFormat }}'
                      InfoIconLabelOptions: null
              Visuals:
                - TableVisual:
                    VisualId: '{{ VisualId }}'
                    Title:
                      Visibility: null
                      FormatText:
                        PlainText: '{{ PlainText }}'
                        RichText: '{{ RichText }}'
                    Subtitle:
                      Visibility: null
                      FormatText:
                        PlainText: '{{ PlainText }}'
                        RichText: '{{ RichText }}'
                    ChartConfiguration:
                      FieldWells:
                        TableAggregatedFieldWells:
                          GroupBy:
                            - NumericalDimensionField:
                                FieldId: '{{ FieldId }}'
                                Column: null
                                HierarchyId: '{{ HierarchyId }}'
                                FormatConfiguration:
                                  FormatConfiguration:
                                    NumberDisplayFormatConfiguration:
                                      Prefix: '{{ Prefix }}'
                                      Suffix: '{{ Suffix }}'
                                      SeparatorConfiguration:
                                        DecimalSeparator: '{{ DecimalSeparator }}'
                                        ThousandsSeparator:
                                          Symbol: null
                                          Visibility: null
                                      DecimalPlacesConfiguration:
                                        DecimalPlaces: null
                                      NumberScale: '{{ NumberScale }}'
                                      NegativeValueConfiguration:
                                        DisplayMode: '{{ DisplayMode }}'
                                      NullValueFormatConfiguration:
                                        NullString: '{{ NullString }}'
                                    CurrencyDisplayFormatConfiguration:
                                      Prefix: '{{ Prefix }}'
                                      Suffix: '{{ Suffix }}'
                                      SeparatorConfiguration: null
                                      Symbol: '{{ Symbol }}'
                                      DecimalPlacesConfiguration: null
                                      NumberScale: null
                                      NegativeValueConfiguration: null
                                      NullValueFormatConfiguration: null
                                    PercentageDisplayFormatConfiguration:
                                      Prefix: '{{ Prefix }}'
                                      Suffix: '{{ Suffix }}'
                                      SeparatorConfiguration: null
                                      DecimalPlacesConfiguration: null
                                      NegativeValueConfiguration: null
                                      NullValueFormatConfiguration: null
                              CategoricalDimensionField:
                                FieldId: '{{ FieldId }}'
                                Column: null
                                HierarchyId: '{{ HierarchyId }}'
                                FormatConfiguration:
                                  NullValueFormatConfiguration: null
                                  NumericFormatConfiguration: null
                              DateDimensionField:
                                FieldId: '{{ FieldId }}'
                                Column: null
                                DateGranularity: '{{ DateGranularity }}'
                                HierarchyId: '{{ HierarchyId }}'
                                FormatConfiguration:
                                  DateTimeFormat: '{{ DateTimeFormat }}'
                                  NullValueFormatConfiguration: null
                                  NumericFormatConfiguration: null
                          Values:
                            - NumericalMeasureField:
                                FieldId: '{{ FieldId }}'
                                Column: null
                                AggregationFunction:
                                  SimpleNumericalAggregation: '{{ SimpleNumericalAggregation }}'
                                  PercentileAggregation:
                                    PercentileValue: null
                                FormatConfiguration: null
                              CategoricalMeasureField:
                                FieldId: '{{ FieldId }}'
                                Column: null
                                AggregationFunction: '{{ AggregationFunction }}'
                                FormatConfiguration: null
                              DateMeasureField:
                                FieldId: '{{ FieldId }}'
                                Column: null
                                AggregationFunction: '{{ AggregationFunction }}'
                                FormatConfiguration: null
                              CalculatedMeasureField:
                                FieldId: '{{ FieldId }}'
                                Expression: '{{ Expression }}'
                        TableUnaggregatedFieldWells:
                          Values:
                            - FieldId: '{{ FieldId }}'
                              Column: null
                              FormatConfiguration:
                                StringFormatConfiguration: null
                                NumberFormatConfiguration: null
                                DateTimeFormatConfiguration: null
                      SortConfiguration:
                        RowSort:
                          - FieldSort:
                              FieldId: '{{ FieldId }}'
                              Direction: '{{ Direction }}'
                            ColumnSort:
                              SortBy: null
                              Direction: null
                              AggregationFunction:
                                NumericalAggregationFunction: null
                                CategoricalAggregationFunction: null
                                DateAggregationFunction: null
                                AttributeAggregationFunction:
                                  SimpleAttributeAggregation: '{{ SimpleAttributeAggregation }}'
                                  ValueForMultipleValues: '{{ ValueForMultipleValues }}'
                        PaginationConfiguration:
                          PageSize: null
                          PageNumber: null
                      TableOptions:
                        Orientation: '{{ Orientation }}'
                        HeaderStyle:
                          Visibility: null
                          FontConfiguration: null
                          TextWrap: '{{ TextWrap }}'
                          HorizontalTextAlignment: '{{ HorizontalTextAlignment }}'
                          VerticalTextAlignment: '{{ VerticalTextAlignment }}'
                          BackgroundColor: '{{ BackgroundColor }}'
                          Height: null
                          Border:
                            UniformBorder:
                              Color: '{{ Color }}'
                              Thickness: null
                              Style: '{{ Style }}'
                            SideSpecificBorder:
                              InnerVertical: null
                              InnerHorizontal: null
                              Left: null
                              Right: null
                              Top: null
                              Bottom: null
                        CellStyle: null
                        RowAlternateColorOptions:
                          Status: '{{ Status }}'
                          RowAlternateColors:
                            - '{{ RowAlternateColors[0] }}'
                          UsePrimaryBackgroundColor: null
                      TotalOptions:
                        TotalsVisibility: null
                        TotalAggregationOptions:
                          - FieldId: '{{ FieldId }}'
                            TotalAggregationFunction:
                              SimpleTotalAggregationFunction: '{{ SimpleTotalAggregationFunction }}'
                        Placement: '{{ Placement }}'
                        ScrollStatus: '{{ ScrollStatus }}'
                        CustomLabel: '{{ CustomLabel }}'
                        TotalCellStyle: null
                      FieldOptions:
                        SelectedFieldOptions:
                          - FieldId: '{{ FieldId }}'
                            Width: '{{ Width }}'
                            CustomLabel: '{{ CustomLabel }}'
                            Visibility: null
                            URLStyling:
                              LinkConfiguration:
                                Target: '{{ Target }}'
                                Content:
                                  CustomTextContent:
                                    Value: '{{ Value }}'
                                    FontConfiguration: null
                                  CustomIconContent:
                                    Icon: '{{ Icon }}'
                              ImageConfiguration:
                                SizingOptions:
                                  TableCellImageScalingConfiguration: '{{ TableCellImageScalingConfiguration }}'
                        Order:
                          - '{{ Order[0] }}'
                        PinnedFieldOptions:
                          PinnedLeftFields:
                            - '{{ PinnedLeftFields[0] }}'
                      PaginatedReportOptions:
                        VerticalOverflowVisibility: null
                        OverflowColumnHeaderVisibility: null
                      TableInlineVisualizations:
                        - DataBars:
                            FieldId: '{{ FieldId }}'
                            PositiveColor: '{{ PositiveColor }}'
                            NegativeColor: '{{ NegativeColor }}'
                    ConditionalFormatting:
                      ConditionalFormattingOptions:
                        - Cell:
                            FieldId: '{{ FieldId }}'
                            TextFormat:
                              BackgroundColor:
                                Solid:
                                  Expression: '{{ Expression }}'
                                  Color: '{{ Color }}'
                                Gradient:
                                  Expression: '{{ Expression }}'
                                  Color:
                                    Stops:
                                      - GradientOffset: null
                                        DataValue: null
                                        Color: '{{ Color }}'
                              TextColor: null
                              Icon:
                                IconSet:
                                  Expression: '{{ Expression }}'
                                  IconSetType: '{{ IconSetType }}'
                                CustomCondition:
                                  Expression: '{{ Expression }}'
                                  IconOptions:
                                    Icon: '{{ Icon }}'
                                    UnicodeIcon: '{{ UnicodeIcon }}'
                                  Color: '{{ Color }}'
                                  DisplayConfiguration:
                                    IconDisplayOption: '{{ IconDisplayOption }}'
                          Row:
                            BackgroundColor: null
                            TextColor: null
                    Actions:
                      - CustomActionId: '{{ CustomActionId }}'
                        Name: '{{ Name }}'
                        Status: null
                        Trigger: '{{ Trigger }}'
                        ActionOperations:
                          - FilterOperation:
                              SelectedFieldsConfiguration:
                                SelectedFields:
                                  - '{{ SelectedFields[0] }}'
                                SelectedFieldOptions: '{{ SelectedFieldOptions }}'
                                SelectedColumns:
                                  - null
                              TargetVisualsConfiguration:
                                SameSheetTargetVisualConfiguration:
                                  TargetVisuals:
                                    - '{{ TargetVisuals[0] }}'
                                  TargetVisualOptions: '{{ TargetVisualOptions }}'
                            NavigationOperation:
                              LocalNavigationConfiguration:
                                TargetSheetId: '{{ TargetSheetId }}'
                            URLOperation:
                              URLTemplate: '{{ URLTemplate }}'
                              URLTarget: null
                            SetParametersOperation:
                              ParameterValueConfigurations:
                                - DestinationParameterName: '{{ DestinationParameterName }}'
                                  Value:
                                    CustomValuesConfiguration:
                                      IncludeNullValue: '{{ IncludeNullValue }}'
                                      CustomValues:
                                        StringValues:
                                          - '{{ StringValues[0] }}'
                                        IntegerValues:
                                          - null
                                        DecimalValues:
                                          - null
                                        DateTimeValues:
                                          - '{{ DateTimeValues[0] }}'
                                    SelectAllValueOptions: '{{ SelectAllValueOptions }}'
                                    SourceParameterName: '{{ SourceParameterName }}'
                                    SourceField: '{{ SourceField }}'
                                    SourceColumn: null
                  PivotTableVisual:
                    VisualId: '{{ VisualId }}'
                    Title: null
                    Subtitle: null
                    ChartConfiguration:
                      FieldWells:
                        PivotTableAggregatedFieldWells:
                          Rows:
                            - null
                          Columns:
                            - null
                          Values:
                            - null
                      SortConfiguration:
                        FieldSortOptions:
                          - FieldId: '{{ FieldId }}'
                            SortBy:
                              Field: null
                              Column: null
                              DataPath:
                                Direction: null
                                SortPaths:
                                  - FieldId: '{{ FieldId }}'
                                    FieldValue: '{{ FieldValue }}'
                                    DataPathType:
                                      PivotTableDataPathType: '{{ PivotTableDataPathType }}'
                      TableOptions:
                        MetricPlacement: '{{ MetricPlacement }}'
                        SingleMetricVisibility: null
                        ColumnNamesVisibility: null
                        ToggleButtonsVisibility: null
                        ColumnHeaderStyle: null
                        RowHeaderStyle: null
                        CellStyle: null
                        RowFieldNamesStyle: null
                        RowAlternateColorOptions: null
                        CollapsedRowDimensionsVisibility: null
                        RowsLayout: '{{ RowsLayout }}'
                        RowsLabelOptions:
                          Visibility: null
                          CustomLabel: '{{ CustomLabel }}'
                        DefaultCellWidth: '{{ DefaultCellWidth }}'
                      TotalOptions:
                        RowSubtotalOptions:
                          TotalsVisibility: null
                          CustomLabel: '{{ CustomLabel }}'
                          FieldLevel: '{{ FieldLevel }}'
                          FieldLevelOptions:
                            - FieldId: '{{ FieldId }}'
                          TotalCellStyle: null
                          ValueCellStyle: null
                          MetricHeaderCellStyle: null
                          StyleTargets:
                            - CellType: '{{ CellType }}'
                        ColumnSubtotalOptions: null
                        RowTotalOptions:
                          TotalsVisibility: null
                          TotalAggregationOptions:
                            - null
                          Placement: null
                          ScrollStatus: null
                          CustomLabel: '{{ CustomLabel }}'
                          TotalCellStyle: null
                          ValueCellStyle: null
                          MetricHeaderCellStyle: null
                        ColumnTotalOptions: null
                      FieldOptions:
                        SelectedFieldOptions:
                          - FieldId: '{{ FieldId }}'
                            CustomLabel: '{{ CustomLabel }}'
                            Visibility: null
                        DataPathOptions:
                          - DataPathList:
                              - null
                            Width: '{{ Width }}'
                        CollapseStateOptions:
                          - Target:
                              FieldId: '{{ FieldId }}'
                              FieldDataPathValues:
                                - null
                            State: '{{ State }}'
                      PaginatedReportOptions:
                        VerticalOverflowVisibility: null
                        OverflowColumnHeaderVisibility: null
                    ConditionalFormatting:
                      ConditionalFormattingOptions:
                        - Cell:
                            FieldId: '{{ FieldId }}'
                            TextFormat: null
                            Scope:
                              Role: '{{ Role }}'
                            Scopes:
                              - null
                    Actions:
                      - null
                  BarChartVisual:
                    VisualId: '{{ VisualId }}'
                    Title: null
                    Subtitle: null
                    ChartConfiguration:
                      FieldWells:
                        BarChartAggregatedFieldWells:
                          Category:
                            - null
                          Values:
                            - null
                          Colors:
                            - null
                          SmallMultiples:
                            - null
                      SortConfiguration:
                        CategorySort:
                          - null
                        CategoryItemsLimit:
                          ItemsLimit: null
                          OtherCategories: '{{ OtherCategories }}'
                        ColorSort:
                          - null
                        ColorItemsLimit: null
                        SmallMultiplesSort:
                          - null
                        SmallMultiplesLimitConfiguration: null
                      Orientation: '{{ Orientation }}'
                      BarsArrangement: '{{ BarsArrangement }}'
                      VisualPalette:
                        ChartColor: '{{ ChartColor }}'
                        ColorMap:
                          - Element: null
                            Color: '{{ Color }}'
                            TimeGranularity: null
                      SmallMultiplesOptions:
                        MaxVisibleRows: null
                        MaxVisibleColumns: null
                        PanelConfiguration:
                          Title:
                            Visibility: null
                            FontConfiguration: null
                            HorizontalTextAlignment: null
                          BorderVisibility: null
                          BorderThickness: '{{ BorderThickness }}'
                          BorderStyle: '{{ BorderStyle }}'
                          BorderColor: '{{ BorderColor }}'
                          GutterVisibility: null
                          GutterSpacing: '{{ GutterSpacing }}'
                          BackgroundVisibility: null
                          BackgroundColor: '{{ BackgroundColor }}'
                        XAxis:
                          Scale: '{{ Scale }}'
                          Placement: '{{ Placement }}'
                        YAxis: null
                      CategoryAxis:
                        TickLabelOptions:
                          LabelOptions: null
                          RotationAngle: null
                        AxisLineVisibility: null
                        GridLineVisibility: null
                        DataOptions:
                          NumericAxisOptions:
                            Scale:
                              Linear:
                                StepCount: null
                                StepSize: null
                              Logarithmic:
                                Base: null
                            Range:
                              MinMax:
                                Minimum: null
                                Maximum: null
                              DataDriven: {}
                          DateAxisOptions:
                            MissingDateVisibility: null
                        ScrollbarOptions:
                          Visibility: null
                          VisibleRange:
                            PercentRange:
                              From: null
                              To: null
                        AxisOffset: '{{ AxisOffset }}'
                      CategoryLabelOptions:
                        Visibility: null
                        SortIconVisibility: null
                        AxisLabelOptions:
                          - FontConfiguration: null
                            CustomLabel: '{{ CustomLabel }}'
                            ApplyTo:
                              FieldId: '{{ FieldId }}'
                              Column: null
                      ValueAxis: null
                      ValueLabelOptions: null
                      ColorLabelOptions: null
                      Legend:
                        Visibility: null
                        Title: null
                        Position: '{{ Position }}'
                        Width: '{{ Width }}'
                        Height: '{{ Height }}'
                      DataLabels:
                        Visibility: null
                        CategoryLabelVisibility: null
                        MeasureLabelVisibility: null
                        DataLabelTypes:
                          - FieldLabelType:
                              FieldId: '{{ FieldId }}'
                              Visibility: null
                            DataPathLabelType:
                              FieldId: '{{ FieldId }}'
                              FieldValue: '{{ FieldValue }}'
                              Visibility: null
                            RangeEndsLabelType:
                              Visibility: null
                            MinimumLabelType:
                              Visibility: null
                            MaximumLabelType:
                              Visibility: null
                        Position: '{{ Position }}'
                        LabelContent: '{{ LabelContent }}'
                        LabelFontConfiguration: null
                        LabelColor: '{{ LabelColor }}'
                        Overlap: '{{ Overlap }}'
                        TotalsVisibility: null
                      Tooltip:
                        TooltipVisibility: null
                        SelectedTooltipType: '{{ SelectedTooltipType }}'
                        FieldBasedTooltip:
                          AggregationVisibility: null
                          TooltipTitleType: '{{ TooltipTitleType }}'
                          TooltipFields:
                            - FieldTooltipItem:
                                FieldId: '{{ FieldId }}'
                                Label: '{{ Label }}'
                                Visibility: null
                              ColumnTooltipItem:
                                Column: null
                                Label: '{{ Label }}'
                                Visibility: null
                                Aggregation: null
                      ReferenceLines:
                        - Status: null
                          DataConfiguration:
                            StaticConfiguration:
                              Value: null
                            DynamicConfiguration:
                              Column: null
                              MeasureAggregationFunction: null
                              Calculation: null
                            AxisBinding: '{{ AxisBinding }}'
                            SeriesType: '{{ SeriesType }}'
                          StyleConfiguration:
                            Pattern: '{{ Pattern }}'
                            Color: '{{ Color }}'
                          LabelConfiguration:
                            ValueLabelConfiguration:
                              RelativePosition: '{{ RelativePosition }}'
                              FormatConfiguration: null
                            CustomLabelConfiguration:
                              CustomLabel: '{{ CustomLabel }}'
                            FontConfiguration: null
                            FontColor: '{{ FontColor }}'
                            HorizontalPosition: '{{ HorizontalPosition }}'
                            VerticalPosition: '{{ VerticalPosition }}'
                      ContributionAnalysisDefaults:
                        - MeasureFieldId: '{{ MeasureFieldId }}'
                          ContributorDimensions:
                            - null
                    Actions:
                      - null
                    ColumnHierarchies:
                      - ExplicitHierarchy:
                          HierarchyId: '{{ HierarchyId }}'
                          Columns:
                            - null
                          DrillDownFilters:
                            - NumericEqualityFilter:
                                Column: null
                                Value: null
                              CategoryFilter:
                                Column: null
                                CategoryValues:
                                  - '{{ CategoryValues[0] }}'
                              TimeRangeFilter:
                                Column: null
                                RangeMinimum: '{{ RangeMinimum }}'
                                RangeMaximum: '{{ RangeMaximum }}'
                                TimeGranularity: null
                        DateTimeHierarchy:
                          HierarchyId: '{{ HierarchyId }}'
                          DrillDownFilters:
                            - null
                        PredefinedHierarchy:
                          HierarchyId: '{{ HierarchyId }}'
                          Columns:
                            - null
                          DrillDownFilters:
                            - null
                  KPIVisual:
                    VisualId: '{{ VisualId }}'
                    Title: null
                    Subtitle: null
                    ChartConfiguration:
                      FieldWells:
                        Values:
                          - null
                        TargetValues:
                          - null
                        TrendGroups:
                          - null
                      SortConfiguration:
                        TrendGroupSort:
                          - null
                      KPIOptions:
                        ProgressBar:
                          Visibility: null
                        TrendArrows:
                          Visibility: null
                        SecondaryValue:
                          Visibility: null
                        Comparison:
                          ComparisonMethod: '{{ ComparisonMethod }}'
                          ComparisonFormat:
                            NumberDisplayFormatConfiguration: null
                            PercentageDisplayFormatConfiguration: null
                        PrimaryValueDisplayType: '{{ PrimaryValueDisplayType }}'
                        PrimaryValueFontConfiguration: null
                        SecondaryValueFontConfiguration: null
                        Sparkline:
                          Visibility: null
                          Type: '{{ Type }}'
                          Color: '{{ Color }}'
                          TooltipVisibility: null
                        VisualLayoutOptions:
                          StandardLayout:
                            Type: '{{ Type }}'
                    ConditionalFormatting:
                      ConditionalFormattingOptions:
                        - PrimaryValue:
                            TextColor: null
                            Icon: null
                          ProgressBar:
                            ForegroundColor: null
                          ActualValue:
                            TextColor: null
                            Icon: null
                          ComparisonValue:
                            TextColor: null
                            Icon: null
                    Actions:
                      - null
                    ColumnHierarchies:
                      - null
                  PieChartVisual:
                    VisualId: '{{ VisualId }}'
                    Title: null
                    Subtitle: null
                    ChartConfiguration:
                      FieldWells:
                        PieChartAggregatedFieldWells:
                          Category:
                            - null
                          Values:
                            - null
                          SmallMultiples:
                            - null
                      SortConfiguration:
                        CategorySort:
                          - null
                        CategoryItemsLimit: null
                        SmallMultiplesSort:
                          - null
                        SmallMultiplesLimitConfiguration: null
                      DonutOptions:
                        ArcOptions:
                          ArcThickness: '{{ ArcThickness }}'
                        DonutCenterOptions:
                          LabelVisibility: null
                      SmallMultiplesOptions: null
                      CategoryLabelOptions: null
                      ValueLabelOptions: null
                      Legend: null
                      DataLabels: null
                      Tooltip: null
                      VisualPalette: null
                      ContributionAnalysisDefaults:
                        - null
                    Actions:
                      - null
                    ColumnHierarchies:
                      - null
                  GaugeChartVisual:
                    VisualId: '{{ VisualId }}'
                    Title: null
                    Subtitle: null
                    ChartConfiguration:
                      FieldWells:
                        Values:
                          - null
                        TargetValues:
                          - null
                      GaugeChartOptions:
                        PrimaryValueDisplayType: null
                        Comparison: null
                        ArcAxis:
                          Range:
                            Min: null
                            Max: null
                          ReserveRange: null
                        Arc:
                          ArcAngle: null
                          ArcThickness: '{{ ArcThickness }}'
                        PrimaryValueFontConfiguration: null
                      DataLabels: null
                      TooltipOptions: null
                      VisualPalette: null
                    ConditionalFormatting:
                      ConditionalFormattingOptions:
                        - PrimaryValue:
                            TextColor: null
                            Icon: null
                          Arc:
                            ForegroundColor: null
                    Actions:
                      - null
                  LineChartVisual:
                    VisualId: '{{ VisualId }}'
                    Title: null
                    Subtitle: null
                    ChartConfiguration:
                      FieldWells:
                        LineChartAggregatedFieldWells:
                          Category:
                            - null
                          Values:
                            - null
                          Colors:
                            - null
                          SmallMultiples:
                            - null
                      SortConfiguration:
                        CategorySort:
                          - null
                        CategoryItemsLimitConfiguration: null
                        ColorItemsLimitConfiguration: null
                        SmallMultiplesSort:
                          - null
                        SmallMultiplesLimitConfiguration: null
                      ForecastConfigurations:
                        - ForecastProperties:
                            PeriodsForward: null
                            PeriodsBackward: null
                            UpperBoundary: null
                            LowerBoundary: null
                            PredictionInterval: null
                            Seasonality: null
                          Scenario:
                            WhatIfPointScenario:
                              Date: '{{ Date }}'
                              Value: null
                            WhatIfRangeScenario:
                              StartDate: '{{ StartDate }}'
                              EndDate: '{{ EndDate }}'
                              Value: null
                      Type: '{{ Type }}'
                      SmallMultiplesOptions: null
                      XAxisDisplayOptions: null
                      XAxisLabelOptions: null
                      PrimaryYAxisDisplayOptions:
                        AxisOptions: null
                        MissingDataConfigurations:
                          - TreatmentOption: '{{ TreatmentOption }}'
                      PrimaryYAxisLabelOptions: null
                      SecondaryYAxisDisplayOptions: null
                      SecondaryYAxisLabelOptions: null
                      DefaultSeriesSettings:
                        AxisBinding: null
                        LineStyleSettings:
                          LineVisibility: null
                          LineInterpolation: '{{ LineInterpolation }}'
                          LineStyle: '{{ LineStyle }}'
                          LineWidth: '{{ LineWidth }}'
                        MarkerStyleSettings:
                          MarkerVisibility: null
                          MarkerShape: '{{ MarkerShape }}'
                          MarkerSize: '{{ MarkerSize }}'
                          MarkerColor: '{{ MarkerColor }}'
                      Series:
                        - FieldSeriesItem:
                            FieldId: '{{ FieldId }}'
                            AxisBinding: null
                            Settings:
                              LineStyleSettings: null
                              MarkerStyleSettings: null
                          DataFieldSeriesItem:
                            FieldId: '{{ FieldId }}'
                            FieldValue: '{{ FieldValue }}'
                            AxisBinding: null
                            Settings: null
                      Legend: null
                      DataLabels: null
                      ReferenceLines:
                        - null
                      Tooltip: null
                      ContributionAnalysisDefaults:
                        - null
                      VisualPalette: null
                    Actions:
                      - null
                    ColumnHierarchies:
                      - null
                  HeatMapVisual:
                    VisualId: '{{ VisualId }}'
                    Title: null
                    Subtitle: null
                    ChartConfiguration:
                      FieldWells:
                        HeatMapAggregatedFieldWells:
                          Rows:
                            - null
                          Columns:
                            - null
                          Values:
                            - null
                      SortConfiguration:
                        HeatMapRowSort:
                          - null
                        HeatMapColumnSort:
                          - null
                        HeatMapRowItemsLimitConfiguration: null
                        HeatMapColumnItemsLimitConfiguration: null
                      RowLabelOptions: null
                      ColumnLabelOptions: null
                      ColorScale:
                        Colors:
                          - Color: '{{ Color }}'
                            DataValue: null
                        ColorFillType: '{{ ColorFillType }}'
                        NullValueColor: null
                      Legend: null
                      DataLabels: null
                      Tooltip: null
                    ColumnHierarchies:
                      - null
                    Actions:
                      - null
                  TreeMapVisual:
                    VisualId: '{{ VisualId }}'
                    Title: null
                    Subtitle: null
                    ChartConfiguration:
                      FieldWells:
                        TreeMapAggregatedFieldWells:
                          Groups:
                            - null
                          Sizes:
                            - null
                          Colors:
                            - null
                      SortConfiguration:
                        TreeMapSort:
                          - null
                        TreeMapGroupItemsLimitConfiguration: null
                      GroupLabelOptions: null
                      SizeLabelOptions: null
                      ColorLabelOptions: null
                      ColorScale: null
                      Legend: null
                      DataLabels: null
                      Tooltip: null
                    Actions:
                      - null
                    ColumnHierarchies:
                      - null
                  GeospatialMapVisual:
                    VisualId: '{{ VisualId }}'
                    Title: null
                    Subtitle: null
                    ChartConfiguration:
                      FieldWells:
                        GeospatialMapAggregatedFieldWells:
                          Geospatial:
                            - null
                          Values:
                            - null
                          Colors:
                            - null
                      Legend: null
                      Tooltip: null
                      WindowOptions:
                        Bounds:
                          North: null
                          South: null
                          West: null
                          East: null
                        MapZoomMode: '{{ MapZoomMode }}'
                      MapStyleOptions:
                        BaseMapStyle: '{{ BaseMapStyle }}'
                      PointStyleOptions:
                        SelectedPointStyle: '{{ SelectedPointStyle }}'
                        ClusterMarkerConfiguration:
                          ClusterMarker:
                            SimpleClusterMarker:
                              Color: '{{ Color }}'
                        HeatmapConfiguration:
                          HeatmapColor:
                            Colors:
                              - Color: '{{ Color }}'
                      VisualPalette: null
                    ColumnHierarchies:
                      - null
                    Actions:
                      - null
                  FilledMapVisual:
                    VisualId: '{{ VisualId }}'
                    Title: null
                    Subtitle: null
                    ChartConfiguration:
                      FieldWells:
                        FilledMapAggregatedFieldWells:
                          Geospatial:
                            - null
                          Values:
                            - null
                      SortConfiguration:
                        CategorySort:
                          - null
                      Legend: null
                      Tooltip: null
                      WindowOptions: null
                      MapStyleOptions: null
                    ConditionalFormatting:
                      ConditionalFormattingOptions:
                        - Shape:
                            FieldId: '{{ FieldId }}'
                            Format:
                              BackgroundColor: null
                    ColumnHierarchies:
                      - null
                    Actions:
                      - null
                  FunnelChartVisual:
                    VisualId: '{{ VisualId }}'
                    Title: null
                    Subtitle: null
                    ChartConfiguration:
                      FieldWells:
                        FunnelChartAggregatedFieldWells:
                          Category:
                            - null
                          Values:
                            - null
                      SortConfiguration:
                        CategorySort:
                          - null
                        CategoryItemsLimit: null
                      CategoryLabelOptions: null
                      ValueLabelOptions: null
                      Tooltip: null
                      DataLabelOptions:
                        Visibility: null
                        CategoryLabelVisibility: null
                        MeasureLabelVisibility: null
                        Position: null
                        LabelFontConfiguration: null
                        LabelColor: '{{ LabelColor }}'
                        MeasureDataLabelStyle: '{{ MeasureDataLabelStyle }}'
                      VisualPalette: null
                    Actions:
                      - null
                    ColumnHierarchies:
                      - null
                  ScatterPlotVisual:
                    VisualId: '{{ VisualId }}'
                    Title: null
                    Subtitle: null
                    ChartConfiguration:
                      FieldWells:
                        ScatterPlotCategoricallyAggregatedFieldWells:
                          XAxis:
                            - null
                          YAxis:
                            - null
                          Category:
                            - null
                          Size:
                            - null
                          Label:
                            - null
                        ScatterPlotUnaggregatedFieldWells:
                          XAxis:
                            - null
                          YAxis:
                            - null
                          Size:
                            - null
                          Category:
                            - null
                          Label:
                            - null
                      XAxisLabelOptions: null
                      XAxisDisplayOptions: null
                      YAxisLabelOptions: null
                      YAxisDisplayOptions: null
                      Legend: null
                      DataLabels: null
                      Tooltip: null
                      VisualPalette: null
                    Actions:
                      - null
                    ColumnHierarchies:
                      - null
                  ComboChartVisual:
                    VisualId: '{{ VisualId }}'
                    Title: null
                    Subtitle: null
                    ChartConfiguration:
                      FieldWells:
                        ComboChartAggregatedFieldWells:
                          Category:
                            - null
                          BarValues:
                            - null
                          Colors:
                            - null
                          LineValues:
                            - null
                      SortConfiguration:
                        CategorySort:
                          - null
                        CategoryItemsLimit: null
                        ColorSort:
                          - null
                        ColorItemsLimit: null
                      BarsArrangement: null
                      CategoryAxis: null
                      CategoryLabelOptions: null
                      PrimaryYAxisDisplayOptions: null
                      PrimaryYAxisLabelOptions: null
                      SecondaryYAxisDisplayOptions: null
                      SecondaryYAxisLabelOptions: null
                      ColorLabelOptions: null
                      Legend: null
                      BarDataLabels: null
                      LineDataLabels: null
                      Tooltip: null
                      ReferenceLines:
                        - null
                      VisualPalette: null
                    Actions:
                      - null
                    ColumnHierarchies:
                      - null
                  BoxPlotVisual:
                    VisualId: '{{ VisualId }}'
                    Title: null
                    Subtitle: null
                    ChartConfiguration:
                      FieldWells:
                        BoxPlotAggregatedFieldWells:
                          GroupBy:
                            - null
                          Values:
                            - null
                      SortConfiguration:
                        CategorySort:
                          - null
                        PaginationConfiguration: null
                      BoxPlotOptions:
                        StyleOptions:
                          FillStyle: '{{ FillStyle }}'
                        OutlierVisibility: null
                        AllDataPointsVisibility: null
                      CategoryAxis: null
                      CategoryLabelOptions: null
                      PrimaryYAxisDisplayOptions: null
                      PrimaryYAxisLabelOptions: null
                      Legend: null
                      Tooltip: null
                      ReferenceLines:
                        - null
                      VisualPalette: null
                    Actions:
                      - null
                    ColumnHierarchies:
                      - null
                  WaterfallVisual:
                    VisualId: '{{ VisualId }}'
                    Title: null
                    Subtitle: null
                    ChartConfiguration:
                      FieldWells:
                        WaterfallChartAggregatedFieldWells:
                          Categories:
                            - null
                          Values:
                            - null
                          Breakdowns:
                            - null
                      SortConfiguration:
                        CategorySort:
                          - null
                        BreakdownItemsLimit: null
                      WaterfallChartOptions:
                        TotalBarLabel: '{{ TotalBarLabel }}'
                      CategoryAxisLabelOptions: null
                      CategoryAxisDisplayOptions: null
                      PrimaryYAxisLabelOptions: null
                      PrimaryYAxisDisplayOptions: null
                      Legend: null
                      DataLabels: null
                      VisualPalette: null
                    Actions:
                      - null
                    ColumnHierarchies:
                      - null
                  HistogramVisual:
                    VisualId: '{{ VisualId }}'
                    Title: null
                    Subtitle: null
                    ChartConfiguration:
                      FieldWells:
                        HistogramAggregatedFieldWells:
                          Values:
                            - null
                      XAxisDisplayOptions: null
                      XAxisLabelOptions: null
                      YAxisDisplayOptions: null
                      BinOptions:
                        SelectedBinType: '{{ SelectedBinType }}'
                        BinCount:
                          Value: null
                        BinWidth:
                          Value: null
                          BinCountLimit: null
                        StartValue: null
                      DataLabels: null
                      Tooltip: null
                      VisualPalette: null
                    Actions:
                      - null
                  WordCloudVisual:
                    VisualId: '{{ VisualId }}'
                    Title: null
                    Subtitle: null
                    ChartConfiguration:
                      FieldWells:
                        WordCloudAggregatedFieldWells:
                          GroupBy:
                            - null
                          Size:
                            - null
                      SortConfiguration:
                        CategoryItemsLimit: null
                        CategorySort:
                          - null
                      CategoryLabelOptions: null
                      WordCloudOptions:
                        WordOrientation: '{{ WordOrientation }}'
                        WordScaling: '{{ WordScaling }}'
                        CloudLayout: '{{ CloudLayout }}'
                        WordCasing: '{{ WordCasing }}'
                        WordPadding: '{{ WordPadding }}'
                        MaximumStringLength: null
                    Actions:
                      - null
                    ColumnHierarchies:
                      - null
                  InsightVisual:
                    VisualId: '{{ VisualId }}'
                    Title: null
                    Subtitle: null
                    InsightConfiguration:
                      Computations:
                        - TopBottomRanked:
                            ComputationId: '{{ ComputationId }}'
                            Name: '{{ Name }}'
                            Category: null
                            Value: null
                            ResultSize: null
                            Type: '{{ Type }}'
                          TopBottomMovers:
                            ComputationId: '{{ ComputationId }}'
                            Name: '{{ Name }}'
                            Time: null
                            Category: null
                            Value: null
                            MoverSize: null
                            SortOrder: '{{ SortOrder }}'
                            Type: null
                          TotalAggregation:
                            ComputationId: '{{ ComputationId }}'
                            Name: '{{ Name }}'
                            Value: null
                          MaximumMinimum:
                            ComputationId: '{{ ComputationId }}'
                            Name: '{{ Name }}'
                            Time: null
                            Value: null
                            Type: '{{ Type }}'
                          MetricComparison:
                            ComputationId: '{{ ComputationId }}'
                            Name: '{{ Name }}'
                            Time: null
                            FromValue: null
                            TargetValue: null
                          PeriodOverPeriod:
                            ComputationId: '{{ ComputationId }}'
                            Name: '{{ Name }}'
                            Time: null
                            Value: null
                          PeriodToDate:
                            ComputationId: '{{ ComputationId }}'
                            Name: '{{ Name }}'
                            Time: null
                            Value: null
                            PeriodTimeGranularity: null
                          GrowthRate:
                            ComputationId: '{{ ComputationId }}'
                            Name: '{{ Name }}'
                            Time: null
                            Value: null
                            PeriodSize: null
                          UniqueValues:
                            ComputationId: '{{ ComputationId }}'
                            Name: '{{ Name }}'
                            Category: null
                          Forecast:
                            ComputationId: '{{ ComputationId }}'
                            Name: '{{ Name }}'
                            Time: null
                            Value: null
                            PeriodsForward: null
                            PeriodsBackward: null
                            UpperBoundary: null
                            LowerBoundary: null
                            PredictionInterval: null
                            Seasonality: '{{ Seasonality }}'
                            CustomSeasonalityValue: null
                      CustomNarrative:
                        Narrative: '{{ Narrative }}'
                    Actions:
                      - null
                    DataSetIdentifier: '{{ DataSetIdentifier }}'
                  SankeyDiagramVisual:
                    VisualId: '{{ VisualId }}'
                    Title: null
                    Subtitle: null
                    ChartConfiguration:
                      FieldWells:
                        SankeyDiagramAggregatedFieldWells:
                          Source:
                            - null
                          Destination:
                            - null
                          Weight:
                            - null
                      SortConfiguration:
                        WeightSort:
                          - null
                        SourceItemsLimit: null
                        DestinationItemsLimit: null
                      DataLabels: null
                    Actions:
                      - null
                  CustomContentVisual:
                    VisualId: '{{ VisualId }}'
                    Title: null
                    Subtitle: null
                    ChartConfiguration:
                      ContentUrl: '{{ ContentUrl }}'
                      ContentType: '{{ ContentType }}'
                      ImageScaling: '{{ ImageScaling }}'
                    Actions:
                      - null
                    DataSetIdentifier: '{{ DataSetIdentifier }}'
                  EmptyVisual:
                    VisualId: '{{ VisualId }}'
                    DataSetIdentifier: '{{ DataSetIdentifier }}'
                    Actions:
                      - null
                  RadarChartVisual:
                    VisualId: '{{ VisualId }}'
                    Title: null
                    Subtitle: null
                    ChartConfiguration:
                      FieldWells:
                        RadarChartAggregatedFieldWells:
                          Category:
                            - null
                          Color:
                            - null
                          Values:
                            - null
                      SortConfiguration:
                        CategorySort:
                          - null
                        CategoryItemsLimit: null
                        ColorSort:
                          - null
                        ColorItemsLimit: null
                      Shape: '{{ Shape }}'
                      BaseSeriesSettings:
                        AreaStyleSettings:
                          Visibility: null
                      StartAngle: null
                      VisualPalette: null
                      AlternateBandColorsVisibility: null
                      AlternateBandEvenColor: '{{ AlternateBandEvenColor }}'
                      AlternateBandOddColor: '{{ AlternateBandOddColor }}'
                      CategoryAxis: null
                      CategoryLabelOptions: null
                      ColorAxis: null
                      ColorLabelOptions: null
                      Legend: null
                      AxesRangeScale: '{{ AxesRangeScale }}'
                    Actions:
                      - null
                    ColumnHierarchies:
                      - null
              TextBoxes:
                - SheetTextBoxId: '{{ SheetTextBoxId }}'
                  Content: '{{ Content }}'
              Layouts:
                - Configuration:
                    GridLayout:
                      Elements:
                        - ElementId: '{{ ElementId }}'
                          ElementType: '{{ ElementType }}'
                          ColumnIndex: null
                          ColumnSpan: null
                          RowIndex: null
                          RowSpan: null
                      CanvasSizeOptions:
                        ScreenCanvasSizeOptions:
                          ResizeOption: '{{ ResizeOption }}'
                          OptimizedViewPortWidth: '{{ OptimizedViewPortWidth }}'
                    FreeFormLayout:
                      Elements:
                        - ElementId: '{{ ElementId }}'
                          ElementType: null
                          XAxisLocation: '{{ XAxisLocation }}'
                          YAxisLocation: '{{ YAxisLocation }}'
                          Width: '{{ Width }}'
                          Height: '{{ Height }}'
                          Visibility: null
                          RenderingRules:
                            - Expression: '{{ Expression }}'
                              ConfigurationOverrides:
                                Visibility: null
                          BorderStyle:
                            Visibility: null
                            Color: '{{ Color }}'
                          SelectedBorderStyle: null
                          BackgroundStyle:
                            Visibility: null
                            Color: '{{ Color }}'
                          LoadingAnimation:
                            Visibility: null
                      CanvasSizeOptions:
                        ScreenCanvasSizeOptions:
                          OptimizedViewPortWidth: '{{ OptimizedViewPortWidth }}'
                    SectionBasedLayout:
                      HeaderSections:
                        - SectionId: '{{ SectionId }}'
                          Layout:
                            FreeFormLayout:
                              Elements:
                                - null
                          Style:
                            Height: '{{ Height }}'
                            Padding:
                              Top: '{{ Top }}'
                              Bottom: '{{ Bottom }}'
                              Left: '{{ Left }}'
                              Right: '{{ Right }}'
                      BodySections:
                        - SectionId: '{{ SectionId }}'
                          Content:
                            Layout: null
                          Style: null
                          PageBreakConfiguration:
                            After:
                              Status: '{{ Status }}'
                      FooterSections:
                        - null
                      CanvasSizeOptions:
                        PaperCanvasSizeOptions:
                          PaperSize: '{{ PaperSize }}'
                          PaperOrientation: '{{ PaperOrientation }}'
                          PaperMargin: null
              SheetControlLayouts:
                - Configuration:
                    GridLayout: null
              ContentType: '{{ ContentType }}'
          CalculatedFields:
            - DataSetIdentifier: '{{ DataSetIdentifier }}'
              Name: '{{ Name }}'
              Expression: '{{ Expression }}'
          ParameterDeclarations:
            - StringParameterDeclaration:
                ParameterValueType: '{{ ParameterValueType }}'
                Name: '{{ Name }}'
                DefaultValues:
                  DynamicValue:
                    UserNameColumn: null
                    GroupNameColumn: null
                    DefaultValueColumn: null
                  StaticValues:
                    - '{{ StaticValues[0] }}'
                ValueWhenUnset:
                  ValueWhenUnsetOption: '{{ ValueWhenUnsetOption }}'
                  CustomValue: '{{ CustomValue }}'
                MappedDataSetParameters:
                  - DataSetIdentifier: '{{ DataSetIdentifier }}'
                    DataSetParameterName: '{{ DataSetParameterName }}'
              DecimalParameterDeclaration:
                ParameterValueType: null
                Name: '{{ Name }}'
                DefaultValues:
                  DynamicValue: null
                  StaticValues:
                    - null
                ValueWhenUnset:
                  ValueWhenUnsetOption: null
                  CustomValue: null
                MappedDataSetParameters:
                  - null
              IntegerParameterDeclaration:
                ParameterValueType: null
                Name: '{{ Name }}'
                DefaultValues:
                  DynamicValue: null
                  StaticValues:
                    - null
                ValueWhenUnset:
                  ValueWhenUnsetOption: null
                  CustomValue: null
                MappedDataSetParameters:
                  - null
              DateTimeParameterDeclaration:
                Name: '{{ Name }}'
                DefaultValues:
                  DynamicValue: null
                  StaticValues:
                    - '{{ StaticValues[0] }}'
                  RollingDate:
                    DataSetIdentifier: '{{ DataSetIdentifier }}'
                    Expression: '{{ Expression }}'
                TimeGranularity: null
                ValueWhenUnset:
                  ValueWhenUnsetOption: null
                  CustomValue: '{{ CustomValue }}'
                MappedDataSetParameters:
                  - null
          FilterGroups:
            - FilterGroupId: '{{ FilterGroupId }}'
              Filters:
                - CategoryFilter:
                    FilterId: '{{ FilterId }}'
                    Column: null
                    Configuration:
                      FilterListConfiguration:
                        MatchOperator: '{{ MatchOperator }}'
                        CategoryValues:
                          - '{{ CategoryValues[0] }}'
                        SelectAllOptions: '{{ SelectAllOptions }}'
                        NullOption: '{{ NullOption }}'
                      CustomFilterListConfiguration:
                        MatchOperator: null
                        CategoryValues:
                          - '{{ CategoryValues[0] }}'
                        SelectAllOptions: null
                        NullOption: null
                      CustomFilterConfiguration:
                        MatchOperator: null
                        CategoryValue: '{{ CategoryValue }}'
                        SelectAllOptions: null
                        ParameterName: '{{ ParameterName }}'
                        NullOption: null
                  NumericRangeFilter:
                    FilterId: '{{ FilterId }}'
                    Column: null
                    IncludeMinimum: '{{ IncludeMinimum }}'
                    IncludeMaximum: '{{ IncludeMaximum }}'
                    RangeMinimum:
                      StaticValue: null
                      Parameter: '{{ Parameter }}'
                    RangeMaximum: null
                    SelectAllOptions: '{{ SelectAllOptions }}'
                    AggregationFunction: null
                    NullOption: null
                  NumericEqualityFilter:
                    FilterId: '{{ FilterId }}'
                    Column: null
                    Value: null
                    SelectAllOptions: null
                    MatchOperator: '{{ MatchOperator }}'
                    AggregationFunction: null
                    ParameterName: '{{ ParameterName }}'
                    NullOption: null
                  TimeEqualityFilter:
                    FilterId: '{{ FilterId }}'
                    Column: null
                    Value: '{{ Value }}'
                    RollingDate: null
                    ParameterName: '{{ ParameterName }}'
                    TimeGranularity: null
                  TimeRangeFilter:
                    FilterId: '{{ FilterId }}'
                    Column: null
                    IncludeMinimum: '{{ IncludeMinimum }}'
                    IncludeMaximum: '{{ IncludeMaximum }}'
                    RangeMinimumValue:
                      StaticValue: '{{ StaticValue }}'
                      RollingDate: null
                      Parameter: '{{ Parameter }}'
                    RangeMaximumValue: null
                    NullOption: null
                    ExcludePeriodConfiguration:
                      Amount: null
                      Granularity: null
                      Status: null
                    TimeGranularity: null
                  RelativeDatesFilter:
                    FilterId: '{{ FilterId }}'
                    Column: null
                    AnchorDateConfiguration:
                      AnchorOption: '{{ AnchorOption }}'
                      ParameterName: '{{ ParameterName }}'
                    MinimumGranularity: null
                    TimeGranularity: null
                    RelativeDateType: '{{ RelativeDateType }}'
                    RelativeDateValue: null
                    ParameterName: '{{ ParameterName }}'
                    NullOption: null
                    ExcludePeriodConfiguration: null
                  TopBottomFilter:
                    FilterId: '{{ FilterId }}'
                    Column: null
                    Limit: null
                    AggregationSortConfigurations:
                      - Column: null
                        SortDirection: null
                        AggregationFunction: null
                    TimeGranularity: null
                    ParameterName: '{{ ParameterName }}'
              ScopeConfiguration:
                SelectedSheets:
                  SheetVisualScopingConfigurations:
                    - SheetId: '{{ SheetId }}'
                      Scope: '{{ Scope }}'
                      VisualIds:
                        - '{{ VisualIds[0] }}'
                AllSheets: {}
              Status: null
              CrossDataset: '{{ CrossDataset }}'
          ColumnConfigurations:
            - Column: null
              FormatConfiguration: null
              Role: '{{ Role }}'
              ColorsConfiguration:
                CustomColors:
                  - FieldValue: '{{ FieldValue }}'
                    Color: '{{ Color }}'
                    SpecialValue: '{{ SpecialValue }}'
          AnalysisDefaults:
            DefaultNewSheetConfiguration:
              InteractiveLayoutConfiguration:
                Grid:
                  CanvasSizeOptions: null
                FreeForm:
                  CanvasSizeOptions: null
              PaginatedLayoutConfiguration:
                SectionBased:
                  CanvasSizeOptions: null
              SheetContentType: null
          Options:
            Timezone: '{{ Timezone }}'
            WeekStart: '{{ WeekStart }}'
      - name: Name
        value: '{{ Name }}'
      - name: Permissions
        value:
          - Principal: '{{ Principal }}'
            Actions:
              - '{{ Actions[0] }}'
      - name: SourceEntity
        value:
          SourceAnalysis:
            Arn: '{{ Arn }}'
            DataSetReferences:
              - DataSetPlaceholder: '{{ DataSetPlaceholder }}'
                DataSetArn: '{{ DataSetArn }}'
          SourceTemplate:
            Arn: '{{ Arn }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: TemplateId
        value: '{{ TemplateId }}'
      - name: ValidationStrategy
        value:
          Mode: '{{ Mode }}'
      - name: VersionDescription
        value: '{{ VersionDescription }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.quicksight.templates
WHERE data__Identifier = '<AwsAccountId|TemplateId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>templates</code> resource, the following permissions are required:

### Create
```json
quicksight:DescribeTemplate,
quicksight:DescribeTemplatePermissions,
quicksight:CreateTemplate,
quicksight:DescribeAnalysis,
quicksight:TagResource,
quicksight:UntagResource,
quicksight:ListTagsForResource
```

### Delete
```json
quicksight:DescribeTemplate,
quicksight:DeleteTemplate
```

### List
```json
quicksight:ListTemplates
```

