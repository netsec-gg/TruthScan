# Contributing to TruthScan

Thank you for your interest in contributing to TruthScan! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please be respectful and constructive in all interactions.

## How Can I Contribute?

### Reporting Bugs

If you encounter a bug, please create an issue in the GitHub repository with the following information:

- A clear, descriptive title
- Steps to reproduce the bug
- Expected behavior
- Actual behavior
- Any error messages or logs
- Environment details (OS, Python version, etc.)

### Suggesting Enhancements

Have an idea for improving TruthScan? We'd love to hear it! Please create an issue that includes:

- A clear, descriptive title
- A detailed description of the enhancement
- How the enhancement would benefit users
- Any relevant examples, screenshots, or mock-ups

### Adding New Data Sources

TruthScan relies on free OSINT data sources. If you know of a valuable data source we're not using:

1. Create an issue describing the data source
2. Include information about the API/access method
3. Explain what kind of data it provides
4. Indicate whether it's free or paid

### Pull Requests

Ready to contribute code? Great! Here's the process:

1. Fork the repository
2. Create a new branch from `main` for your changes
3. Make your changes (following our coding standards)
4. Add tests if applicable
5. Ensure all tests pass
6. Submit a pull request

## Development Setup

To set up a development environment:

1. Clone your forked repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Install development dependencies
   ```
4. Run tests:
   ```bash
   pytest
   ```

## Coding Standards

- Follow PEP 8 guidelines
- Write docstrings for all functions, classes, and modules
- Include type hints where appropriate
- Write unit tests for new functionality
- Use meaningful variable and function names

## Documentation

Good documentation is essential. Please:

- Update the README.md if your changes affect usage
- Document new features or changed behavior
- Add docstrings to new code
- Include example usage where helpful

## New Feature Guidelines

When implementing new features:

1. **Free-first approach**: Ensure features prioritize free alternatives before paid options
2. **Modularity**: Implement features in a modular way that allows easy extension
3. **Compatibility**: Maintain backward compatibility when possible
4. **Error handling**: Include robust error handling and fallback mechanisms
5. **Documentation**: Document how to use the new feature

## Adding New Analysis Modules

If you're adding a new analysis module:

1. Follow the existing class structure pattern
2. Implement the required methods (analyze, generate_summary, etc.)
3. Add appropriate error handling and fallback mechanisms
4. Update the main TruthScan class to include your module
5. Document the new module in README.md

## License

By contributing to TruthScan, you agree that your contributions will be licensed under the project's MIT License.

## Questions?

If you have any questions about contributing, please create an issue with your question, and we'll be happy to help! 